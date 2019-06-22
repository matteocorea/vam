import unittest
from unittest.mock import patch, MagicMock, call
import datastore

class TestDataTransformer(unittest.TestCase):

    def __build_mock_with_structure(self, db, collection, mongo_mock):
        collection_mock = MagicMock()
        db_struct = {}
        db_struct[db] = {}
        db_struct[db][collection] = collection_mock
        client_mock = MagicMock()
        client_mock.__getitem__.side_effect = db_struct.__getitem__
        mongo_mock.return_value = client_mock
        return collection_mock

    @patch('datastore.MongoClient')
    def test_connect_to_the_right_database_and_port(self, mongo_mock):
        datastore.DataStore(host='somewhere.com', port=12345)
        mongo_mock.assert_called_once_with(host='mongodb://somewhere.com', port=12345)

    @patch('datastore.MongoClient')
    def test_saves_to_the_right_db_and_collection_with_prefix(self, mongo_mock):
        collection_mock = (
            self.__build_mock_with_structure('some_test_db', 'some_nice_prefix_12345', mongo_mock))
        
        store = datastore.DataStore(dbname='some_test_db', collection_prefix='some_nice_prefix_')
        store.save(['foo'], 12345)
        collection_mock.insert_one.assert_called_once()
        
    @patch('datastore.MongoClient')
    def test_saves_the_right_data_to_the_db(self, mongo_mock):
        collection_mock = (
            self.__build_mock_with_structure('testdb', 'streamdata_12345', mongo_mock))
        
        store = datastore.DataStore()
        store.save(['foo', 'bar', 'baz'], 12345)
        calls = [call('foo'), call('bar'), call('baz')]
        collection_mock.insert_one.assert_has_calls(calls)
        
    @patch('datastore.MongoClient')
    def test_count_messages_on_db_for_stream(self, mongo_mock):
        collection_mock = (
            self.__build_mock_with_structure('testdb', 'streamdata_4321', mongo_mock))
        
        store = datastore.DataStore()
        store.count_messages(4321)
        collection_mock.count_documents.assert_called_once_with({})

if __name__ == '__main__':
    unittest.main()