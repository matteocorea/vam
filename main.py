import sys
from datastore import DataStore
from streamfetcher import StreamFetcher
from datatransformer import DataTransformer

def main():
    if (len(sys.argv) != 2):
        print "Usage: {} streamid".format(sys.argv[0])
        exit(1)
    stream_id = sys.argv[1]
    
    fetcher = StreamFetcher()
    data_store = DataStore()
    transformer = DataTransformer()
    
    data = fetcher.fetch_stream(stream_id, 2, 4)
    data = transformer.transform_data(data)
    data_store.save(data)

main()
