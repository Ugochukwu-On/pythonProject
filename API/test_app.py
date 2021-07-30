import unittest
import API


class TestApp(unittest.TestCase):
    def setUp(self):

        self.client = API.create_app().test_client()


    def test_GET(self):
       rv = self.Notes.get('/Notes')
       assert isinstance(rv.json, object)
       assert'List of Notes' in rv.json


if __name__ == "__main__":
    unittest.main()



