import unittest
import time
from src.app import app


class TestAppIntegration(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        # Could add resource setup here (e.g., DB connection)

    def tearDown(self):
        # Cleanup resources here if needed
        pass

    def test_home(self):
        start = time.time()
        response = self.client.get('/')
        duration = time.time() - start

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {"message": "Hello, World!"})
        self.assertLess(duration, 1, "Response took too long")

    def test_feature_1_default(self):
        response = self.client.get('/feature-1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {"message": "Feature 1"})

    def test_feature_1_with_name(self):
        response = self.client.get('/feature-1?name=ChatGPT')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {"message": "Feature 1"})

    def test_404(self):
        response = self.client.get('/non-existent-route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
