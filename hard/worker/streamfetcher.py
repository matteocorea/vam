import urllib.request
import json

class StreamFetcher:
	"""Fetch data from a remote ONA stream by id.
	
	This implements the whole data retrieval logic, including batching."""
	
	def fetch_stream(self, stream_number, start, batch_size):
		"""Fetch data from a stream, returning a data batch with given start."""
		
		url = (f"https://api.ona.io/api/v1/data/{stream_number}?start={start}&limit={batch_size}")
		data = urllib.request.urlopen(url).read()
		jsondata = json.loads(data)
		return jsondata