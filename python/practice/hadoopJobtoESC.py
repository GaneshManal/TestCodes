import json
import sys
from yarn_api_client import ApplicationMaster, HistoryServer, NodeManager, ResourceManager

resource_manager = ResourceManager(address="192.168.100.205", port=8088)
app_master = ApplicationMaster(address="192.168.100.205", port=8088)

if len(sys.argv) > 1:
    app_id = sys.argv[1]
else:
    print 'Need app-id as an input.'
    sys.exit(0)

print 'App Id: ', app_id

app = resource_manager.cluster_application(app_id).data.get('app')
print 'App Details: ', json.dumps(app)

print '=' * 100
jobs = app_master.jobs(app.get('id')).data.get('jobs').get('job')
print 'Job Details :', json.dumps(jobs)

print '-' * 100
for job in jobs:
    task = app_master.job_tasks(app.get('id'), job.get('id')).data
    print 'Task Details:', json.dumps(task)
