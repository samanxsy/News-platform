import unittest
from flask import Flask
import app.common.status as status
import app.server as server


class BaseTest(unittest.TestCase):
    """Base test for calling the app from flask, and testing the routes"""
    def setUp(self):
        self.app = Flask("Your o News", static_folder='./app/static', template_folder='./app/templates')
        self.app.add_url_rule('/', view_func=server.home)


class TestRoutes(BaseTest):
    """Test the routes"""

    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)