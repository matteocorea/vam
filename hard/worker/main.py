import sys
from datastore import DataStore
from streamfetcher import StreamFetcher
from datatransformer import DataTransformer

def main():
    if (len(sys.argv) != 2):
        print "Usage: {} streamid".format(sys.argv[0])
        exit(1)
    stream_id = sys.argv[1]
    
    batch_size = 30     # could be made configurable
    
    fetcher = StreamFetcher()
    data_store = DataStore()
    transformer = DataTransformer()
    
    first_record = data_store.count_messages(stream_id)
    data = fetcher.fetch_stream(stream_id, first_record, batch_size)
    data = transformer.transform_data(data)
    data_store.save(data, stream_id)

main()
