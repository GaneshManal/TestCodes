from elasticsearch import Elasticsearch
import sys
import json
import pprint
from elasticsearch.exceptions import ConnectionError, ConnectionTimeout, TransportError


class ElasticsearchDS:

    def __init__(self, port=9200, host="10.11.0.199", username=None, password=None, timeout=20):
        auth_default = None if username is None else (username, password)
        try:
            self.es = Elasticsearch([{"host": host, "port": port, 'http_auth': None}],
                                    timeout=timeout)
            print self.es
        except (ConnectionError, ConnectionTimeout) as es_err:
            print 'Error: %s', es_err

    def es_get_mapping(self, index=None, doc_type=None):
        schema = self.es.indices.get_mapping(index=index, doc_type=doc_type)
        return schema

    def es_get_indices(self):
        schema = self.es_get_mapping()
        indices_details = schema.keys()
        list_of_indices = [index for index in indices_details if not index.startswith(".")]
        return list_of_indices

    def es_exec_query(self, index=None, doc_type=None, query=None):
        res = self.es.search(index=index, doc_type=doc_type, body=query)
        print("%d documents found" % res['hits']['total'])
        return res

es_obj = ElasticsearchDS()
print es_obj

# Get mapping
print " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAPPING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
es_mapping = es_obj.es_get_mapping()
print es_mapping

print " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAPPING : collector_2eee16b4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
es_mapping = es_obj.es_get_mapping("collector_2eee16b4")
print es_mapping

print " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Indices >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
es_indices = es_obj.es_get_indices()
print es_indices

# Exe query
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> QUERY:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
query = {
    "size": 0,
    "aggs": {
        "collector_b0125de5": {
            "terms": {
                "field": "hostName.keyword"
            }
        }
    }
}
res = es_obj.es_exec_query(index="collector_b0125de5", query=query)
pprint.pprint(res)


# Copy Index
# es_obj.copy_index(index = "collector_b60aa132", doc_type ="new_doc_type")
