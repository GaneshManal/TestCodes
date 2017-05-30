from Queue import Queue
from threading import Thread
import salt.client
import os, time

start = time.clock()

local = salt.client.LocalClient()
q = Queue()


def is_node_up(node):
    status = dict()
    try:
        # status = local.cmd(tgt=node, fun="test.ping")
        cmd = 'salt ' + node + ' test.ping'
        proc = os.popen(cmd)
        ret = proc.read()
        if 'True' in ret:
            status = {node: True}

        if 'Not connected' in ret:
            status = {node: False}

    except Exception as e:
        status = {node: False}

    q.put(status)
    print "Ping Complete -", node

node_list = ["ubuntu1", "ubuntu2", "ubuntu3"]
for each_node in node_list:
    Thread(target=is_node_up, args=[each_node]).start()

while True:
    # print 'Que Content', q.qsize()
    if q.qsize() >= len(node_list):
        print 'Received the status for all nodes.'
        break

print time.clock() - start
# Printing Queue
while True:
    print q.get()

    if q.empty():
        break
