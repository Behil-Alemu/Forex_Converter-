from app import app
import unittest

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_(self):
        response = self.client.get('/convert?amount=10')
        self.assertIn(b'136', response.data)
        self.assertEqual(response.status_code, 200)