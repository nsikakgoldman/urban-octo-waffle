import unittest
import threading
import time
from simple_socket import start_server
from simple_client import send_data_to_server

class TestServer(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=start_server, args=('127.0.0.1', 65432))
        self.server_thread.daemon = True
        self.server_thread.start()
        time.sleep(1)# give some time for the server to start


    def test_server_response(self):
        response = send_data_to_server('127.0.01', 65432, 'TestMessage')# so the hello is coming from the server being tested
        self.assertEqual(response, 'Hello, TestMessage')

if __name__ == "__main__":
    unittest.main