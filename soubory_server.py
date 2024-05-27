import socket
import threading
import os

def handle_client(client_socket, addr):
    print(f'Připojen nový klient: {addr}')
    while True:
        command = client_socket.recv(1024).decode()
        if command == 'SEND_FILE':
            file_name = client_socket.recv(1024).decode()
            file_size = int(client_socket.recv(1024).decode())
            client_socket.send('CONFIRM'.encode())
            confirmation = client_socket.recv(1024).decode()
            if confirmation == 'YES':
                with open(f'received_{file_name}', 'wb') as f:
                    bytes_received = 0
                    while bytes_received < file_size:
                        data = client_socket.recv(1024)
                        f.write(data)
                        bytes_received += len(data)
                client_socket.send('TRANSFER_COMPLETE'.encode())
            else:
                client_socket.send('TRANSFER_ABORTED'.encode())
        elif command == 'EXIT':
            break

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print('Server naslouchá na portu 5555')

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == '__main__':
    main()
