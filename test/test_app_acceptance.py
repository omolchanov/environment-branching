import unittest
from src.app import app


class TestAppAcceptance(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        """Simulate a user visiting the home page."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertEqual(response.json["message"], "Hello, World!")

    def test_feature_1_flow(self):
        """Simulate a user visiting the feature-1 page with and without a query param."""
        # Without query param
        response = self.client.get('/feature-1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Feature 1")

        # With query param
        response = self.client.get('/feature-1?name=Tester')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Feature 1")


if __name__ == '__main__':
    unittest.main()
