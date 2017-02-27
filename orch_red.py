
import json
from kafka import KafkaClient
import multiprocessing
import os
import sys
import time

# User defined imports
sys.path.append(os.getcwd())
from collector.collector_manager import CollectorManager
from const import *
from orchestrator.logger.plugin import FluentdPluginManager
import outils
from poller.pollerm import PollerManager
import settings
from util import di_logging

#logger handle
log = di_logging(ORCHESTRATOR)


class Template:

    def __init__(self):
        self.template = {}
        self.template_id = ""
        self.es_index_map = []

    def init_existing_template(self, template_id, template):
        log.debug("Init existing: template_id- %s, template- %s" % (template_id, template))
        self.template = template
        self.template_id = template_id

    def init_template(self, template):
        tid = os.urandom(4).encode('hex')
        tname = template[NAME]
        log.debug("Init: template_id- %s, template- %s" % (tid, template))
        entry = {TEMPLATE_NAME: tname, TEMPLATE_ID: tid, STATUS: INIT}
        if outils.add_to_template_map(entry):
            # set components
            self.template_id = tid
            self.template = template
            if self._build_data_path():
                if self._save_template():
                    return self.template_id
        return None

    def _build_data_path(self):
        # Work here for elasticsearch, Index are explicitly created with mappings
        mapping = {}
        mapping_collector = {}
        mapping_logger = {}
        mapping_poller = {}
        try:
            with open(os.path.join(MAPPINGS_FILE_PATH, COLLECTOR_MAPPING)) as fh:
                mapping_collector = json.load(fh)
            log.debug("Collector mapping: %s" % mapping_collector)
        except IOError:
            log.error("No Mapping for collector index found")
            return False
        try:
            with open(os.path.join(MAPPINGS_FILE_PATH, LOGGER_MAPPING)) as fh:
                mapping_logger = json.load(fh)
            log.debug("Logger mapping: %s" % mapping_logger)
        except IOError:
            log.error("No Mapping for logger index found")
            return False

        for cluster in self.template.get(CLUSTERS, []):
            write_target_cl = []
            write_target_lg = []
            write_target_pl = []
            collectors = cluster.get(AGENTS, {}).get(COLLECTORS)
            if collectors:
                worker_list = collectors.get(PLUGINS, [])
                for worker in worker_list:
                    write_target_cl += worker.get(WRITE_TARGETS, [])
            loggers = cluster.get(AGENTS, {}).get(LOGGERS)
            if loggers:
                worker_list = loggers.get(PLUGINS, [])
                for worker in worker_list:
                    write_target_lg += worker.get(WRITE_TARGETS, [])
            poller = cluster.get(POLLER)
            if poller:
                worker_list = poller.get(PLUGINS, [])
                for worker in worker_list:
                    write_target_pl += worker.get(WRITE_TARGETS, [])
            target_list = self.template.get(TARGETS, {}).get(PLUGINS, [])
            if target_list:
                for target in target_list:
                    if target.get(TYPE, '') == ES:
                        mapping = {}
                        target_name = target.get(NAME, '')
                        log.debug("Target- %s is of type elastic search" % (target_name))
                        if target_name in write_target_pl:
                            target = target.get(META, {})
                        client = "%s:%s" % (target.get(HOST, '127.0.0.1'), target.get(PORT, '9200'))
                        index = target.get(INDEX, TEMP_INDEX)
                        ds_type = target.get(DS_TYPE, TEMP_DS)
                        if {HOST: client, INDEX: index, DS_TYPE: ds_type} in self.es_index_map:
                            log.debug("Mapping for host- %s, index- %s, ds_type- %s already exists" % (client, index, ds_type))
                            continue
                        if target_name in write_target_cl:
                            log.debug("Target found in collector list")
                            mapping[MAPPINGS] = {ds_type: mapping_collector[MAPPINGS][COLLECTD]}
                        if target_name in write_target_lg:
                            log.debug("Target found in logger list")
                            mapping[MAPPINGS] = {ds_type: mapping_logger[MAPPINGS][FLUENTD]}
                        if target_name in write_target_pl:
                            log.debug("Target found in poller list")
                            mapping_file_name = ''
                            for worker in poller.get(PLUGINS, []):
                                for target in worker.get(WRITE_TARGETS, []):
                                    if target == target_name:
                                        mapping_file_name = worker.get(NAME, '')
                                        break
                            if mapping_file_name:
                                log.debug("Mapping file name: %s" %(mapping_file_name))
                                if 1:
                                    with open(os.path.join(MAPPINGS_FILE_PATH, mapping_file_name)) as fh:
                                        mapping_poller = json.load(fh)
                                        mapping[MAPPINGS] = {ds_type: mapping_poller[MAPPINGS][POLLER_TYPE]}
                                        log.debug("Poller mapping: %s" % (mapping_poller))
                                else:
                                #except IOError:
                                    log.error("No Mapping for poller plugin")
                                    for item in self.es_index_map:
                                        outils.delete_es_index(item[HOST], item[INDEX])
                                    return False
                        if mapping:
                            #create mapping here
                            if outils.create_es_index(client, index, ds_type, mapping):
                                self.es_index_map.append({HOST: client, INDEX: index, DS_TYPE: ds_type})
                            else:
                                log.error("No Mapping for poller plugin")
                                for item in self.es_index_map:
                                    outils.delete_es_index(item[HOST], item[INDEX])
                                return False
        return True

    def get_template(self):
        log.debug("get_template- 1")
        return self.template

    def _save_template(self):
        file_path = os.path.join(os.getcwd(), ORCHESTRATOR,
                                 TEMPLATE_FILE_PATH, self.template_id)
        return outils.write_to_file(file_path, self.template)

    # template operations
    def _get_path(self, cluster_name="", op_level="", worker_name=""):
        update_path =  None
        if not cluster_name:
            if not op_level:
                if not worker_name:
                    update_path = self.template
                else:
                    log.error("worker_name can not exist without cluster_name/op_level")
            else:
                if op_level == TARGETS:
                    if not worker_name:
                        update_path = self.template.get(op_level)
                    else:
                        worker_list = self.template.get(op_level, {}).get(PLUGINS)
                        if worker_list:
                            for worker in worker_list:
                                if worker[NAME] == worker_name:
                                    update_path = worker
                                    break
                else:
                    log.error("If cluster_name is empty op_level should be targets")
        else:
            cluster = {}
            cluster_list = self.template.get(CLUSTERS, [])
            for cluster in cluster_list:
                if cluster[NAME] == cluster_name:
                    break
            if cluster:
                if not op_level:
                    update_path = cluster
                else:
                    if op_level == COLLECTORS or op_level == LOGGERS:
                        update_path = cluster.get(AGENTS, {}).get(op_level)
                    if op_level == POLLER:
                        update_path = cluster.get(op_level)
                    if worker_name:
                        worker_list = update_path.get(PLUGINS, {})
                        for worker in worker_list:
                            if worker_name == worker[NAME]:
                                update_path = worker
                                break
            else:
                log.error("No cluster found to update")
        return update_path

    def update_template_attr(self, attr, value, cluster_name="", op_level="", worker_name="", sub_op=ADD):
        status = False
        if not self.template:
            log.error("Template is empty, can not update attributes")
            return status
        update_path = self._get_path(cluster_name, op_level, worker_name)
        if update_path:
            if attr == INTERVAL or attr == FILTER_LEVEL or attr == META or attr == ENABLE:
                try:
                    update_path[attr] = value
                    status = True
                except KeyError:
                    log.error("Attribute- %s is not present in give path" %(attr))
            if attr == TAGS or attr == NODE_LIST or attr == WRITE_TARGETS:
                try:
                    if sub_op == ADD or sub_op == UPDATE:
                        update_path[attr].append(value)
                    if sub_op == CLEAR:
                        update_path[attr] = []
                    if sub_op == DELETE:
                        if value in update_path[attr]:
                            update_path[attr].remove(value)
                    status = True
                except KeyError:
                    log.error("Attribute- %s is not present in give path" %(attr))
        else:
            log.error("No update_path found")
        if status:
            return self._save_template()

    def enable_template(self, value=True, cluster_name="", op_level="", worker_name=""):
        if not self.template:
            log.error("Template is empty, can not perform enable operations")
            return False
        if not cluster_name and not op_level:
            self.template[ENABLE] = value
            self.template[TARGETS][ENABLE] = value
            worker_list = self.template.get(TARGETS).get(PLUGINS)
            if worker_list:
                for worker in worker_list:
                    worker[ENABLE] = value
            cluster_list = self.template.get(CLUSTERS)
            if cluster_list:
                for cluster in cluster_list:
                    cluster[ENABLE] = value
                    collector = cluster.get(AGENTS, {}).get(COLLECTORS)
                    if collector:
                        collector[ENABLE] = value
                        worker_list = collector.get(PLUGINS, [])
                        for worker in worker_list:
                            worker[ENABLE] = value
                    logger = cluster.get(AGENTS, {}).get(LOGGERS)
                    if logger:
                        logger[ENABLE] = value
                        worker_list = logger.get(PLUGINS, [])
                        for worker in worker_list:
                            worker[ENABLE] = value
                    poller = cluster.get(POLLER)
                    if poller:
                        poller[ENABLE] = value
                        worker_list = poller.get(PLUGINS,[])
                        for worker in worker_list:
                            worker[ENABLE] = value
            return self._save_template()
        else:
            return self.update_template_attr(ENABLE, value, cluster_name, op_level, worker_name)

    def get_template_attr(self, attr="", cluster_name="", op_level="", worker_name=""):
         value = None
         update_path = _get_path(cluster_name, op_level, worker_name)
         if update_path:
             if attr:
                 value = update_path.get(attr)
             else:
                 value = update_path
         else:
             log.error()
         return value

    def delete_worker(self, worker_name, op_level, cluster_name=""):
        status = False
        item = get_attr(cluster_name, op_level)
        if item:
            worker_list = item.get(op_level).get(PLUGINS)
            if worker_list:
                for worker in worker_list:
                    if worker[NAME] == worker_name:
                        if not worker[ENABLE]:
                            worker_list.remove(worker)
                            status = self._save_template()
                        else:
                            log.error("Set enable to false and redeploy before deleting plugin")
                        break


    def add_worker(self, worker, op_level, cluster_name=""):
        status = False
        item = get_attr(cluster_name, op_level)
        if item:
            worker_list = item.get(op_level).get(PLUGINS)
            if worker_list:
                worker_list.append(worker)
                status = self._save_template()
        return status

    def _get_specific_targets(self, worker_list, targets):
        x_targets = []
        for worker in worker_list:
            target_list = worker.get(WRITE_TARGETS)
            if target_list:
                for target_name in target_list:
                    found = False
                    for x_target in targets:
                        if x_target[ENABLE] and target_name == x_target[NAME]:
                            if x_target not in x_targets:
                                x_targets.append(x_target)
                            found = True
                    if not found:
                        log.error("Target- %s for plugin- %s not found" % (target_name, worker[NAME]))
        return x_targets

    def _get_data(self, targets, global_tags, node_list, module, op_level):
        data = {}
        if op_level != POLLER:
            data.update({NODE_LIST: node_list})
            data.update({TAGS: global_tags})
        else:
            for plugin in module.get(PLUGINS, []):
                try:
                    plugin[TAGS] += global_tags
                except:
                    log.error("Can not update poller plugin tags")
        data.update({op_level: module})
        data[op_level].update({TARGETS: targets})
        return data

    def _get_expanded_profile(self, collector):
        log.debug("get_expanded_profile- 1")
        template_prof = dict(collector)
        template_prof[PLUGINS] = []
        plugin_map = {}
        plugins = []
        file_path = os.path.join(os.getcwd(), ORCHESTRATOR,
                             PROFILE_PATH, "profile")
        with open(file_path, 'r') as fh:
            plugin_map = json.load(fh)
        worker_list = collector.get(PLUGINS, {})
        for worker in worker_list:
            if worker.get(PROFILE, False):
                for plugin_name in plugin_map[worker[NAME]]:
                    new_plugin = dict(worker)
                    new_plugin[NAME] = plugin_name
                    template_prof[PLUGINS].append(new_plugin)
            else:
                template_prof[PLUGINS].append(dict(worker))
        log.debug("get_expanded_profile- 2: template_prof- %s" % (template_prof))
        return template_prof

    def _set_list_enable(self, value, list_t):
        for item in list_t:
            try:
                item[ENABLE] = item[ENABLE] and value
            except KeyError:
                log.debug("Key- %s was not found in %s, defaulting to True" % (ENABLE, item[NAME]))
                item[ENABLE] = True

    # Exec operations
    def _call_service(self, template, op_level, op, dirty_list=[]):
        return multiprocessing.Process(target=self._service, args=(template, op_level, op, dirty_list))

    def _service(self, template, op_level, op, dirty_list=[]):
        log.info("Module called- %s with op- %s" % (op_level, op))
        if op_level == COLLECTORS:
            cm_obj = CollectorManager(template)
            if op == REFRESH:
                cm_obj.deploy()
            if op == TEARDOWN:
                cm_obj.teardown()
        elif op_level == LOGGERS:
            lg_obj = FluentdPluginManager(template)
            if op == REFRESH:
                if template.get(ENABLE, True):
                    lg_obj.deploy(START)
                else:
                    lg_obj.deploy(STOP)
            if op == TEARDOWN:
                lg_obj.teardown()
        elif op_level == POLLER:
            pm_obj = PollerManager("tempid", template)
            if op == DEPLOY:
                pm_obj.deploy()
            if op == STOP:
                pm_obj.stop(dirty_list)
            if op == START:
                pm_obj.update(dirty_list)
            if op == TEARDOWN:
                pm_obj.teardownall()
        else:
            log.error("Undefined module")

    def exec_template(self, op=DEPLOY, cluster_name="", op_level=""):
        if not self.template:
            log.error("Template is empty, can not execute it")
            return False
        if (cluster_name and op_level == TARGETS):
            log.error("With sub template op_level should be either collectos, loggers, pollers")
            return False
        if op == DEPLOY:
            proc = self._call_service({}, POLLER, DEPLOY)
            proc.start()
            return True
        template = dict(self.template)
        ena_t = template.get(ENABLE, True)
        outils.update_template_map(self.template_id, ena_t)
        targets = template.get(TARGETS, {}).get(PLUGINS,{})
        self._set_list_enable(ena_t, targets)
        global_tags = template.get(TAGS, [])
        node_list = []
        poller_dep_targets = []
        cm_proc = None
        lg_proc = None
        #perform operation for each cluster or for cluster_name
        cluster_list = template.get(CLUSTERS,[])
        for cluster in cluster_list:
            node_list = cluster.get(AGENTS,{}).get(NODE_LIST)
            if not cluster_name or cluster_name == cluster[NAME]:
                #call collector services
                if node_list:
                    collector = cluster.get(AGENTS, {}).get(COLLECTORS)
                    if collector:
                        #set enable parameter
                        ena_c = ena_t and collector.get(ENABLE, True)
                        if not op_level  or op_level == COLLECTORS:
                            worker_list = collector.get(PLUGINS,[])
                            if worker_list:
                                #set enable parameter for each plugin
                                self._set_list_enable(ena_c, worker_list)
                                #expand profile
                                collector_exp = self._get_expanded_profile(collector)
                                #get targets specific to collector
                                x_targets = self._get_specific_targets(worker_list, targets)
                                data = self._get_data(x_targets, global_tags, node_list, collector_exp, COLLECTORS)
                                log.debug("Deploy collector with data- %s" %(data))
                                cm_proc = self._call_service(data, COLLECTORS, op)
                                log.debug("Starting collector process- %s" % (time.time))
                                cm_proc.start()
                                #log.debug("Deploy collector with global_tags- %s, node_list- %s, targets- %s, collector -%s" %(global_tags, node_list, targets, collector))
                    #call logger services
                    logger = cluster.get(AGENTS,{}).get(LOGGERS)
                    if logger:
                        #set enable parameter
                        ena_l = ena_t and logger.get(ENABLE, True)
                        if not op_level  or op_level == LOGGERS:
                            worker_list = logger.get(PLUGINS, [])
                            if worker_list:
                                #set enable parameter for each plugin
                                self._set_list_enable(ena_c, worker_list)
                                #get targets specific to collector
                                x_targets = self._get_specific_targets(worker_list, targets)
                                data = self._get_data(x_targets, global_tags, node_list, logger, LOGGERS)
                                lg_proc = self._call_service(data, LOGGERS, op)
                                log.debug("Starting logger process- %s" % (time.time))
                                lg_proc.start()
                                log.debug("Deploy logger with global_tags- %s, node_list- %s, targets- %s, logger -%s" %(global_tags, node_list, targets, logger))
                else:
                    log.error("Node list is empty for cluster- %s, can not deploy agents" % (cluster[NAME]))
                #call poller services
                poller = cluster.get(POLLER)
                if poller:
                    if op == TEARDOWN:
                        log.debug("Teardown Poller")
                        #call teardown all
                        pm_proc = self._call_service({}, POLLER, op)
                    else:
                        #set poller enable parameter
                        ena_p = ena_t and poller.get(ENABLE, True)
                        worker_list = poller.get(PLUGINS)
                        x_targets = self._get_specific_targets(worker_list, targets)
                        print x_targets
                        if worker_list:
                            #set enable parameter for each plugin
                            self._set_list_enable(ena_p, worker_list)
                            update_list = []
                            stop_list = []
                            for worker in worker_list:
                                if worker.get(ENABLE, True):
                                    update_list.append(worker.get(NAME, ''))
                                else:
                                    stop_list.append(worker.get(NAME, ''))
                        for worker in x_targets:
                            if worker.get(ENABLE, True):
                                #do not redeploy targets/remember they are global
                                if worker[NAME] not in poller_dep_targets:
                                    update_list.append(worker.get(NAME, ''))
                                    poller_dep_targets.append(worker.get(NAME, ''))
                            else:
                                if worker[NAME] not in poller_dep_targets:
                                    stop_list.append(worker.get(NAME, ''))
                        data = self._get_data(x_targets, global_tags, [], poller, POLLER)
                        if stop_list:
                            pm_proc = self._call_service(data, POLLER, STOP, dirty_list=stop_list)
                            log.debug("Poller Stop called with- %s and dirty list- %s" %(data, stop_list))
                            pm_proc.start()
                            pm_proc.join()
                        if update_list:
                            pm_proc = self._call_service(data, POLLER, START, dirty_list=update_list)
                            log.debug("Poller Start called with- %s and dirty list- %s" %(data, update_list))
                            print("Poller Start called with- %s and dirty list- %s" %(data, update_list))
                            pm_proc.start()
                            pm_proc.join()
        if lg_proc:
            log.debug("Waiting on logger process")
            lg_proc.join()
            log.debug("Exiting logger process- %s" %(time.time))
        if cm_proc:
            log.debug("Waiting on collector process")
            cm_proc.join()
            log.debug("Exiting collector process- %s" %(time.time))
        return True

    def teardown_template(self):
        # pull down whole monitoring infra
        log.debug("Teardown template: template- %s" % self.template)
        if self.exec_template(op=TEARDOWN):
            if outils.remove_from_template_map(self.template_id):
                for item in self.es_index_map:
                    outils.delete_es_index(item[HOST], item[INDEX])

    #get calls
    '''
    def get_template_status_monitoring(self):
        log.debug("Get template status monitoring- 1")
        # call get status of all modules or fetch from db
        template_status = {}
        template_status.update({NAME: self.template_name})
        template_status.update({TEMPLATE_ID: self.template_id})
        # collector/logger check status
        cluster_status = []
        cluster_list = self.template.get(CLUSTERS):
        if cluster_list:
            for cluster in cluster_list
            data = dict()
            data.update({NAME: cluster[NAME]})
            data.update({NODE_LIST: cluster[NODE_LIST]})
            data.update({COLLECTORS:_get_status(NODE_LIST,  self._check_status())})
        # update poller status
        poller_status = self.pm.check_status()
        plugin_status = []
        target_status = []
        for plugin in self.template.get(POLLER, {}).get(PLUGINS, []):
            status = NOT_RUNNING
            for item in poller_status:
                if item[NAME] == plugin[NAME]:
                    if item[STATUS]:
                        status = RUNNING
            temp = {NAME: plugin[NAME], STATUS: status}
            plugin_status.append(temp)
        for target in self.template.get(POLLER, {}).get(TARGETS, []):
            status = NOT_RUNNING
            for item in poller_status:
                if item[NAME] == plugin[NAME]:
                    if item[STATUS]:
                        status = RUNNING
            temp = {NAME: target[NAME], STATUS: status}
            target_status.append(temp)

        template_status.update({POLLER: {PLUGINS: plugin_status, TARGETS: target_status}})
        template_status.update({SUB_TEMPLATE: cluster})
        log.debug("Get template status monitoring- 2: %s" % (template_status))
        return template_status
    '''


def get_template_obj(template_id):
    if not template_id:
        return None
    temp = outils.get_template_stored(template_id)

    if temp:
        template = Template()
        template.init_existing_template(template_id, temp)
        return template
    else:
        return None

data = ""
with open("orchestrator/template.json", "r") as fh:
   data = json.load(fh)
t = Template()
tid = t.init_template(data)
print tid
t.enable_template(value=True)
t.exec_template(op=DEPLOY)
time.sleep(60)
t.exec_template(op=REFRESH)
t.update_template_attr(TAGS, "tag1", cluster_name="ALL NODES", op_level="collectors", worker_name="linux_dynamic")
#print outils.get_template_stored(tid)
#t.teardown_template()
