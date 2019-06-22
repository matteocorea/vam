import unittest
from unittest.mock import patch, Mock
import streamfetcher

class TestDataTransformer(unittest.TestCase):

    def setUp(self):
        self.fetcher = streamfetcher.StreamFetcher()

    @patch('streamfetcher.urllib.request')
    def test_decodes_the_result_from_server(self, mock_request):
        urlopen_mock = Mock()
        urlopen_mock.read.return_value = '["foo"]'
        mock_request.urlopen.return_value = urlopen_mock
        res = self.fetcher.fetch_stream(12345, 52, 46)
        self.assertEqual(res, ['foo'])
        
    @patch('streamfetcher.urllib.request')
    def test_calls_server_with_right_params(self, mock_request):
        urlopen_mock = Mock()
        urlopen_mock.read.return_value = '["unused"]'
        mock_request.urlopen.return_value = urlopen_mock
        self.fetcher.fetch_stream(12345, 52, 46)
        expected_url = 'https://api.ona.io/api/v1/data/12345?start=52&limit=46'
        mock_request.urlopen.assert_called_once_with(expected_url)

if __name__ == '__main__':
    unittest.main()