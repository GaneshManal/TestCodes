import sys
import time
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
id = 0


def write_for_hour(time_now, x_hours, rec_per_hr, host_count):
    for item in range(x_hours, 0, -1):
        print("+" + "-" * 100 + "+")
        print("Add record for %s-%s hrs range" % (item, item - 1))

        hosts = ['A', 'B', 'C', 'D']
        delta_minutes = 10

        x_time = time_now - timedelta(hours=item)
        print("Time: %s" % x_time.strftime('%Y-%m-%d %H:%M:%S'))

        for item in range(rec_per_hr):
            x_time = x_time + timedelta(minutes=delta_minutes)

            for host_idx in range(host_count):
                global id
                id += 1

                print("id: %s, time: %s" %(id, x_time.strftime('%Y-%m-%d %H:%M:%S')))
                es.index(index='di_test_data_1',
                         doc_type='dknow',
                         id=id,
                         body={'hostName': hosts[host_idx], 'time': time.mktime(x_time.timetuple()),
                               'CPU_Util': 20, 'MEM_Util': 30, "plugin": "tcpstats"})


es = None
es_conn = "http://10.11.0.199:9200/"
try:
    es = Elasticsearch([es_conn])
except Exception as err:
    print("Exception: %s", str(err))
    sys.exit(1)

hours_count = int(input("Hown Many Hours ?"))
rec_per_hr = int(input("How Many records per hour ?"))
host_count = int(input("Hown Many Hosts ?"))


time_now = datetime.now()
print("Current Time: %s" % time_now.strftime('%Y-%m-%d %H:%M:%S'))
write_for_hour(time_now, hours_count, rec_per_hr, host_count)
