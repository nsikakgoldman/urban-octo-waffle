import unittest
from simple_client import send_data_to_server

class TestClient(unittest.TestCase):
    def test_client_response(self):
        response = send_data_to_server('127.0.0.1', 65432, 'TestMessage')
        self.assertEqual(response, 'Hello, TestMessage')

if __name__ == "__main__":
    unittest.main()