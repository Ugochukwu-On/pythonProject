import unittest
from API import app


class TestApp(unittest.TestCase):
    def test_Get(self):
        tester = app.test_request(self)
        response = tester.get('/Notes')
        status_codes = response.status_code
        self.assertEqual((status_codes, 201))

if __name__ == "__main__":
    unittest.main()



