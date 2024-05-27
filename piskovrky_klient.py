import socket

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (len(row) * 4 - 3))

# Připojení ke serveru
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Hlavní smyčka klienta
while True:
    response = client.recv(1024).decode()
    print(response)

    if 'Your turn' in response:
        move = input('Enter your move (row col): ')
        client.send(move.encode())
    elif 'wins' in response or 'Draw' in response or 'Game aborted' in response:
        break
