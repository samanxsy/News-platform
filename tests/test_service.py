import unittest
import app.service as service


class TestService(unittest.TestCase):
    def test_news(self):
        service.news('Bitcoin', 'us')
        self.assertIsNotNone(True)