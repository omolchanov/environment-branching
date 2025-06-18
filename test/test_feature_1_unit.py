import unittest
from src.app import app


class BasicFlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_feature_1_route(self):
        response = self.client.get('/feature-1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Feature 1"})


if __name__ == '__main__':
    unittest.main()
