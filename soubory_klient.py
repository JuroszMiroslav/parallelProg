import socket
import os

def send_file(client_socket, file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client_socket.send('SEND_FILE'.encode())
    client_socket.send(file_name.encode())
    client_socket.send(str(file_size).encode())

    confirmation = client_socket.recv(1024).decode()
    if confirmation == 'CONFIRM':
        print(f'Server čeká na potvrzení přenosu souboru {file_name} ({file_size} bytes).')
        confirm = input('Chcete pokračovat s přenosem souboru? (YES/NO): ')
        client_socket.send(confirm.encode())
        if confirm == 'YES':
            with open(file_path, 'rb') as f:
                while (data := f.read(1024)):
                    client_socket.send(data)
            print(client_socket.recv(1024).decode())
        else:
            print(client_socket.recv(1024).decode())

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    while True:
        command = input('Zadejte příkaz (SEND_FILE/EXIT): ')
        if command == 'SEND_FILE':
            file_path = input('Zadejte cestu k souboru: ')
            send_file(client, file_path)
        elif command == 'EXIT':
            client.send('EXIT'.encode())
            break

    client.close()

if __name__ == '__main__':
    main()
