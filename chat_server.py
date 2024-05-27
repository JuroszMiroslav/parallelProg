import socket
import threading

# Ukládání připojených klientů
clients = {}


def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            client_socket.send(message)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break


def remove_client(client_socket):
    if client_socket in clients:
        client_socket.close()
        del clients[client_socket]


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(10)
    print('Server naslouchá na portu 5555')

    while True:
        client_socket, client_address = server.accept()
        print(f'Připojen nový klient: {client_address}')

        client_socket.send('USERNAME'.encode())
        username = client_socket.recv(1024).decode()
        client_socket.send('PASSWORD'.encode())
        password = client_socket.recv(1024).decode()

        if username and password:
            clients[client_socket] = username
            print(f'{username} se připojil do chatovací místnosti.')
            broadcast(f'{username} se připojil do chatovací místnosti.'.encode(), client_socket)
            client_socket.send('Připojen k serveru.'.encode())
            threading.Thread(target=handle_client, args=(client_socket,)).start()
        else:
            client_socket.close()


if __name__ == '__main__':
    main()
