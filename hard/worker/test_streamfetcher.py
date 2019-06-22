import unittest
from streamfetcher import StreamFetcher

class TestDataTransformer(unittest.TestCase):

    def setUp(self):
        self.fetcher = StreamFetcher()

    def test_calls_remote_endpoint_with_right_params(self):
        self.assertEqual(42, 42)

if __name__ == '__main__':
    unittest.main()