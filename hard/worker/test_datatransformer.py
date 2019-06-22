import unittest
from datatransformer import DataTransformer

class TestDataTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = DataTransformer()

    def test_return_what_is_given(self):
        datum = {'foo': ['bar', 'baz'], 'secret': 42}
        self.assertEqual(self.transformer.transform_data(datum), datum)

if __name__ == '__main__':
    unittest.main()