import urllib2
import json

class StreamFetcher:
	"""Fetch data from a remote ONA stream by id.
	
	This implements the whole data retrieval logic, including batching."""
	
	def fetch_stream(self, stream_number, start, batch_size):
		"""Fetch data from a stream, returning a data batch with given start."""
		
		url = "https://api.ona.io/api/v1/data/{}?start={}&limit={}".format(stream_number, start, batch_size)
		data = urllib2.urlopen(url).read()
		jsondata = json.loads(data)
		return jsondata