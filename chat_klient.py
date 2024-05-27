import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    username = input('Zadejte uživatelské jméno: ')
    password = input('Zadejte heslo: ')

    client.send(username.encode())
    client.send(password.encode())

    response = client.recv(1024).decode()
    if response == 'Připojen k serveru.':
        print(response)
        threading.Thread(target=receive_messages, args=(client,)).start()

        while True:
            message = input()
            if message.lower() == 'exit':
                client.close()
                break
            client.send(f'{username}: {message}'.encode())
    else:
        print('Připojení se nezdařilo.')

if __name__ == '__main__':
    main()
