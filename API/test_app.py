import unittest
from API.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()



    def test_GET_Notes(self):
        tester = app.test_client(self)
        response = tester.get("/Notes")
        status_code = response.status_code
        self.assertEqual(status_code,200)

    def test_POST_new_notes(self):
        #Notes_list = dict(id=4, body="Yo")
        tester = app.test_client(self)
        requests = tester.get('/Notes')
        requests.post({'id': 4, 'body': "yo"})
        status_code = requests.status_code
        self.assertEqual(status_code,200)


if __name__ == "__main__":
    unittest.main()
