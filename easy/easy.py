import sys
import logging
import urllib2
import json
from pymongo import MongoClient

def main():
    """Read all the data from a remote dataset, and save it into a db
    
    This easy solution is anyway parameterized on the dataset id, so that
    the solution can be reused as needed for other datasets. The database host
    and ports could also be included in the parameters, if needed."""
    if (len(sys.argv) != 2):
            print "Usage: {} streamid".format(sys.argv[0])
            exit(1)
    stream_id = sys.argv[1]
        
    data = urllib2.urlopen("https://api.ona.io/api/v1/data/{}".format(stream_id)).read()
    jsondata = json.loads(data)
    
    client = MongoClient()
    for datum in jsondata:
        try:
            client.testdb.easycollection.insert_one(datum)
        except:
            logging.error('could not save message with id "{}"'.format(datum['_id']))
    
main()