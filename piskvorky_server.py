import socket
import threading

# Konstanty pro hru
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 3

# Inicializace herní desky
def init_board():
    return [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Zobrazení herní desky
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (BOARD_SIZE * 4 - 3))

# Kontrola vítěze
def check_winner(board, player):
    # Kontrola řádků, sloupců a diagonál
    for i in range(BOARD_SIZE):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(BOARD_SIZE)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or all([board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)]):
        return True
    return False

# Kontrola remízy
def check_draw(board):
    return all([cell != EMPTY for row in board for cell in row])

# Hlavní funkce pro hru
def game(client1, client2):
    board = init_board()
    current_player = PLAYER_X
    players = {PLAYER_X: client1, PLAYER_O: client2}
    names = {client1: "Player 1", client2: "Player 2"}

    while True:
        for player, client in players.items():
            client.send(f'Your turn ({player})'.encode())
            move = client.recv(1024).decode()
            x, y = map(int, move.split())

            if board[x][y] == EMPTY:
                board[x][y] = player
                if check_winner(board, player):
                    for c in players.values():
                        c.send(f'{names[client]} ({player}) wins!'.encode())
                    return
                if check_draw(board):
                    for c in players.values():
                        c.send('Draw!'.encode())
                    return

                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
                for c in players.values():
                    print_board(board)
            else:
                client.send('Invalid move. Try again.'.encode())

# Funkce pro zpracování klientů
def handle_client(client_socket, client_address):
    client_socket.send('Waiting for another player...'.encode())
    client_socket, client_address = server.accept()
    client_socket.send('Another player connected. Do you want to start the game? (yes/no)'.encode())
    response = client_socket.recv(1024).decode()

    if response.lower() == 'yes':
        client_socket.send('Game starting...'.encode())
        game(client_socket, client_socket)
    else:
        client_socket.send('Game aborted.'.encode())
        client_socket.close()

# Inicializace serveru
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(2)
print('Server is listening on port 5555')

# Čekání na připojení klientů
while True:
    client_socket, client_address = server.accept()
    print(f'Accepted connection from {client_address}')
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
