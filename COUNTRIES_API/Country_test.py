import unittest
from COUNTRIES_API.app import app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_GET_ALL_JSON(self):
        tester = app.test_client(self)
        response = tester.get("/all")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_GET_ALL_COUNTRIES(self):
        tester = app.test_client(self)
        response = tester.get("/country")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_GET_ALL_STATES(self):
        tester = app.test_client(self)
        response = tester.get("/country/states")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/country/states")
        self.assertEqual(response.content_type, "application/json")






if __name__ == '__main__':
    unittest.main()
