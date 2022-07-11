from app import app
import unittest
from currency import Currencies
import flask

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_EUR(self):
        response = self.client.get('/result?from=USD&to=EUR&amount=10')
        self.assertIn(b'9.84', response.data)
        self.assertEqual(response.status_code, 200)
    def test_ISK(self):
        response = self.client.get('/result?from=USD&to=ISK&amount=10')
        self.assertIn(b'1372.63', response.data)
        self.assertEqual(response.status_code, 200)

    def test_back_home(self):
        with app.test_client() as client:
            resp = client.get("/return-home")
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/")

    def test_root(self):
        with app.test_client() as client:
            # can now make requests to flask via `client`
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Start Converting</h1>', html)

    def test_check_valid_from(self):
            with app.test_request_context('/result?from=USD'):
                assert flask.request.path == '/result'
                assert flask.request.args['from'] == 'USD'
                
    def test_check_valid_to(self):
            with app.test_request_context('/result?to=USD'):
                assert flask.request.path == '/result'
                assert flask.request.args['to'] == 'USD'

    def test_check_amount(self):
       with app.test_request_context('/result?amount=10'):
                assert flask.request.path == '/result'
                assert flask.request.args['amount'] == '10'

    def test_converter(self):
        response = self.client.get('/result?from=USD&to=ISK&amount=10')
        self.assertEqual(Currencies().converter('USD','ISK',10), 1372.63)

        


