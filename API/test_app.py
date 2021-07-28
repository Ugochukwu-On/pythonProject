import unittest
from API import app


class TestApp(unittest.TestCase):
    def test_if_not_Get(self):
        x = app.Notes('/Notes', ['GET', 'POST'])
        self.assertEqual(x.Notes, 'GET')


if __name__ == '__main__':
    unittest.main()
