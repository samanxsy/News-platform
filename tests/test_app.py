import unittest
from unittest.mock import patch
from flask import Flask
import app.common.status as status
import app.app as app


class BaseTest(unittest.TestCase):
    """Base test for calling the app from flask, and testing the routes"""
    def setUp(self):
        self.app = Flask("YourO News", static_folder='./app/static', template_folder='./app/templates')
        self.app.add_url_rule('/', view_func=app.home)
        self.app.add_url_rule('/search', view_func=app.search)
        self.app.add_url_rule('/health', view_func=app.health)
        self.app.add_url_rule('/technology', view_func=app.technology)
        self.app.add_url_rule('/business', view_func=app.business)
        self.app.add_url_rule('/science', view_func=app.science)
        self.app.add_url_rule('/entertainment', view_func=app.entertainment)
        self.app.add_url_rule('/sports', view_func=app.sports)
        self.app.add_url_rule('/general', view_func=app.general)


class TestRoutes(BaseTest):
    """This class is used for testing the routes responses"""
    def test_home(self):
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_search(self):
        """This should test the search route and return a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/search')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


#    def test_search_something(self):
#        """This should test the search route with a search query and return the result related to the search and a 200 response"""
#        with self.app.test_client() as c:
#            with patch('requests.get') as mock_get:
#                mock_get.return_value.status_code = 200
#                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
#                response = c.get('/search?search=Apple')
#                self.assertEqual(response.status_code, status.HTTP_200_OK)
#                self.assertIn(b"Apple", response.data)


    def test_health(self):
        """This should test the health route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/health')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_technology(self):
        """This should test the technology route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/technology')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_business(self):
        """This should test the business route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/business')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_science(self):
        """This should test the science route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/science')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_entertainment(self):
        """This should test the entertainment route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/entertainment')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_sports(self):
        """This should test the sports route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/sports')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)


    def test_general(self):
        """This should test the general route and return data with a 200 response"""
        with self.app.test_client() as c:
            with patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {'status': 'ok', 'articles': []}
                response = c.get('/general')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIsNotNone(response.data)