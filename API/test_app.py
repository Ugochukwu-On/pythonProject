import unittest
from API.app import app
from app import Notes_list

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()


    def test_GET(self):
        tester = app.test_client(self)
        response = tester.get("/Notes")
        status_code = response.status_code
        self.assertEqual(status_code,200)

    def test_POST(self):
        tester = app.test_client(self)
        response = tester.post('/Notes/<int:id>',
        Notes_list (
            [
             {
              "id": 2,
              "body": "Yesterday was a good day",
              }
            ]

         ))

        status_code = response.status_code
        self.assertEqual(status_code,200)


if __name__ == "__main__":
    unittest.main()
