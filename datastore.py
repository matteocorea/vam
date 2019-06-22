from pymongo import MongoClient

class DataStore:
    def __init__(self, host='localhost', port=27017):
        self.host = 'mongodb://{}'.format(host)
        self.port = port
        self.db = 'testdb'
        self.collection = 'testcollection'
    
    def save(self, data):
        client = MongoClient(host=self.host, port=self.port)
        client[self.db][self.collection].insert_many(data)