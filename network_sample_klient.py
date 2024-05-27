import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    client_socket.sendall(b'Hello, Server!')
    response = client_socket.recv(1024)
    print(f'Received: {response.decode()}')
    client_socket.close()

if __name__ == '__main__':
    start_client()