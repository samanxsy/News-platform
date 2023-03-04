import unittest
from flask import Flask
import app.common.status as status
import app.app as app


class BaseTest(unittest.TestCase):
    """Base test for calling the app from flask, and testing the routes"""
    def setUp(self):
        self.app = Flask("YourO News", static_folder='./app/static', template_folder='./app/templates')
        self.app.add_url_rule('/', view_func=app.home)
        self.app.add_url_rule('/search', view_func=app.search, methods=['GET'])
        self.app.add_url_rule('/business', view_func=app.business, methods=['GET'])
        self.app.add_url_rule('/business/country', view_func=app.business_country, methods=['GET'])


class TestRoutes(BaseTest):
    """Test the routes"""
    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_search(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/search?search=apple')
            self.assertIsNotNone(response.data)


    def test_business(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/business')
            self.assertIsNotNone(response.data)
