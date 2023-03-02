import unittest
from flask import Flask
import app.common.status as status
import app.app as app


class BaseTest(unittest.TestCase):
    """Base test for calling the app from flask, and testing the routes"""
    def setUp(self):
        self.app = Flask("Your o News", static_folder='./app/static', template_folder='./app/templates')
        self.app.add_url_rule('/', view_func=app.home)
        self.app.add_url_rule('/news', view_func=app.news, methods=['GET'])


class TestRoutes(BaseTest):
    """Test the routes"""

    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)


    def test_news(self):
        with self.app.test_client() as c:
            response = c.get('/news?interest=&country=us')
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.data)

