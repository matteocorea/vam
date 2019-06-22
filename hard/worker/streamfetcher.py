import urllib.request
import json

class StreamFetcher:
	"""Fetch data from a remote ONA stream by id.
	
	This implements the whole data retrieval logic, including batching."""
	
	def fetch_stream(self, stream_number, start, batch_size):
		"""Fetch data from a stream, returning a data batch with given start.
		
		:param stream_number: Integer id of the stream to fetch
		:param start: Integer index of the first message to fetch from the stream.
		:param batch_size: Integer number of messages to be retrieved (upper bound)
		:return: List of messages as retrieved from the stream and JSON decoded
		"""
		
		url = (f"https://api.ona.io/api/v1/data/{stream_number}?start={start}&limit={batch_size}")
		data = urllib.request.urlopen(url).read()
		jsondata = json.loads(data)
		return jsondata