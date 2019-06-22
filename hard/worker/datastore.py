import logging
from pymongo import MongoClient

class DataStore:
    """Handle connection with the db, and all storage needs."""
    
    def __init__(self, host='localhost', port=27017, collection_prefix='streamdata_',
                 dbname='testdb'):
        """Build an instance of Data Store, with already preconfigured db coordinates.
        
        :param host: String database hostname
        :param port: Integer database port number
        :param collection_prefix: String Prefix for the database stream collections
        """
        self.collection_prefix = collection_prefix
        client = MongoClient(host=(f'mongodb://{host}'), port=port)
        self.db = client[dbname]
    
    def __get_collection(self, stream_id):
        """Return the collection needed to access data for a given stream.
        
        :param stream_id: Integer id of the stream we need to create a collection for
        :return: Collection MongoDB object representing the collection for the given stream
        """
        
        collection_name = '{}{}'.format(self.collection_prefix, stream_id)
        return self.db[collection_name]
    
    def save(self, data, stream_id):
        """Save a batch of data into the db.
        
        This method saves each record separately, accepting
        failures (almost) silently. This is to guarantee that
        all the records will be processed and potentially inserted.
        
        :param data: Array of data to be saved to the database
        :param stream_id: Integer id of the stream that generated the data
        """
        
        collection = self.__get_collection(stream_id)
        for datum in data:
            try:
                collection.insert_one(datum)
            except:
                logging.error('could not save message with id "{}"'.format(datum['_id']))

    def count_messages(self, stream_id):
        """Count how many messages are already saved for a single stream.
        
        :param stream_id: Integer id of the stream whose messages we want to count
        :return: Integer number of messages already stored for the given stream
        """
        
        collection = self.__get_collection(stream_id)
        return collection.count_documents({})
        