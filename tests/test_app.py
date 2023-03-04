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
        self.app.add_url_rule('/business/countries', view_func=app.business_countries, methods=['GET'])


class TestRoutes(BaseTest):
    """Test the routes"""
    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_search(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/search?search=apple')
            self.assertIsNotNone(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)
            
            response = c.get('/search?search=ChatGPT and microsoft')
            self.assertIsNotNone(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_health(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/health')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_health_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/health/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/health/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/health/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

    def test_technology(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/technology')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_techonology_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/technology/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/technology/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/technology/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_business(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/business')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_business_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/business/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/business/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/business/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_sciences(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/sciences')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_sciences_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/sciences/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)
            
            response = c.get('/sciences/countries?country=gb')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/sciences/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


            response = c.get('/sciences/countries?country=de')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_entertainment(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/entertainment')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_entertainment_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/entertainment/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/entertainment/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/entertainment/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_sports(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/sports')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_sports_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/sports/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/sports/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/sports/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_general(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/general')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)


    def test_general_countries(self):
        """This function country in the query strings and expects a 200 response and business news related to the country"""
        with self.app.test_client() as c:
            response = c.get('/general/countries?country=us')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/general/countries?country=hu')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)

            response = c.get('/general/countries?country=fr')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)
