from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q, Index
import json


class ElasticSearchDS:
    
    def __init__(self, host='localhost', port=9200, protocol='http'):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.es_client = None
        self.connect()

    def connect(self):
        connection_url = self.protocol+'://'+self.host+":"+str(self.port)
        self.es_client = Elasticsearch(connection_url)
        print 'CLusters: ', json.dumps(self.es_client.cluster.get_settings())
        print 'STatus: ', json.dumps(self.es_client.cluster.stats())
        print 'SEttings: ', json.dumps(self.es_client.cluster.get_settings())

    def get_indices(self):
        return json.dumps(self.es_client.indices.get_mapping().keys())

    def get_mapping(self, index, doc_type = None):
        index_details = self.es_client.indices.get_mapping(index = index, doc_type = doc_type)
        return json.dumps(index_details)

    def get_index_details(self, index, doc_type = None):
        index_details = self.es_client.indices.get_settings(index = index)
        return json.dumps(index_details) 

    def execute_query(self, index ,query):
        s = Search(using=self.es_client).query(index=index)


if __name__ == '__main__':
    esds = ElasticSearchDS(host="10.11.0.199")
    print "Indices :: ", esds.get_indices()

    print "Connector::\n", esds.get_index_details(index='collector_b60aa132', doc_type = "COLLECTD")
