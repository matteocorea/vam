import sys
import urllib2
import json
from pymongo import MongoClient

if (len(sys.argv) != 2):
        print "Usage: {} streamid".format(sys.argv[0])
        exit(1)
stream_id = sys.argv[1]
    
data = urllib2.urlopen("https://api.ona.io/api/v1/data/{}".format(stream_id)).read()
jsondata = json.loads(data)
client = MongoClient()
client.testdb.easycollection.insert_many(jsondata)