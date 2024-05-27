import unittest
from unittest.mock import patch, MagicMock
import socket


class TestNetwork(unittest.TestCase):

    @patch('socket.socket')
    def test_client(self, mock_socket):
        mock_instance = mock_socket.return_value
        mock_instance.recv.return_value = b'Hello, Client!'

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))
        client_socket.sendall(b'Hello, Server!')
        response = client_socket.recv(1024)

        self.assertEqual(response, b'Hello, Client!')
        mock_instance.connect.assert_called_with(('localhost', 9999))
        mock_instance.sendall.assert_called_with(b'Hello, Server!')


if __name__ == '__main__':
    unittest.main()
