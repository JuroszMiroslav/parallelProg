import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print('Server is listening on port 9999')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')
        data = client_socket.recv(1024)
        print(f'Received: {data.decode()}')
        client_socket.sendall(b'Hello, Client!')
        client_socket.close()


if __name__ == '__main__':
    start_server()