import json
import pyelasticsearch as pyes


class ElasticSearchDataSource:

    def __init__(self):
        # Data store details ( to be configured by user )
        self.host = '10.11.0.199'
        self.port = '9200'
        self.es_obj = None
        self.connect()

    def connect(self):
        self.es_obj = pyes.ElasticSearch(["http://" + self.host + ":" + self.port])

    def get_schemas(self):
        return self.es_obj.get_mapping()

    def list_indexes(self):
        return self.es_obj.get_mapping().keys()

    def get_settings(self):
        return self.es_obj.get_settings('logger_b60aa132')

ds_obj = ElasticSearchDataSource()

# Get schema details.
print '+' + '-' * 100 + 'Schemas' + '-' * 100 + '+'
all_schema = ds_obj.get_schemas()
print 'hi'
print json.dumps(all_schema)

# Get All indexes.
print '+' + '-' * 100 + 'indexes' + '-' * 100 + '+'
all_indexes = ds_obj.list_indexes()
print json.dumps(all_indexes), len(all_indexes)

# Print Settings.
print '+' + '-' * 100 + 'Settings' + '-' * 100 + '+'
print json.dumps(ds_obj.get_settings())

print '+' + '-' * 100 + '***' + '-' * 100 + '+'