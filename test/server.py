import socket
import threading

# Khởi tạo kết nối socket
HOST = '127.0.0.1'  # Địa chỉ IP hoặc tên máy chủ
PORT = 12345  # Cổng kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối máy chủ đến địa chỉ và cổng đã chỉ định
server_socket.bind((HOST, PORT))
server_socket.listen()

# Danh sách các kết nối (máy khách)
connections = []

# Biến trạng thái trò chơi
game_started = False
current_player = 'X'

# Bảng lưu trạng thái của bàn cờ
ROWS = 15
COLS = 15
board = [['' for _ in range(COLS)] for _ in range(ROWS)]

# Hàm gửi dữ liệu đến tất cả máy khách
def send_to_all(message):
    for connection in connections:
        connection.send(message.encode())

# Hàm xử lý trò chơi
def game_thread(connection, player):
    global game_started, current_player

    if player == 'X':
        connection.send("You are Player X. Waiting for another player to join...".encode())
        while len(connections) < 2:
            pass
        connection.send("Both players are connected. Game is starting.".encode())
        game_started = True
        send_to_all("Game is starting. Player X goes first.")
    
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break

        row, col = map(int, data.split(','))
        if board[row][col] == '' and player == current_player:
            board[row][col] = player
            current_player = 'O' if current_player == 'X' else 'X'
            move = f"{row},{col}"
            send_to_all(move)

            # Kiểm tra chiến thắng và hòa cờ
            if check_winner(row, col, player):
                send_to_all(f"Player {player} wins!")
                reset_game()
            elif check_draw():
                send_to_all("It's a draw!")
                reset_game()

# Hàm kiểm tra chiến thắng
def check_winner(row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 4 hướng kiểm tra
    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
            else:
                break
        for i in range(1, 5):
            r, c = row - i * dr, col - i * dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# Hàm kiểm tra hòa cờ (đã đầy bàn cờ và không có người thắng)
def check_draw():
    return all(board[i][j] != '' for i in range(ROWS) for j in range(COLS)) and not any(check_winner(i, j, 'X') or check_winner(i, j, 'O') for i in range(ROWS) for j in range(COLS))

# Hàm reset trò chơi
def reset_game():
    global board, current_player, game_started
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 'X'
    game_started = False

# Hàm xử lý kết nối từ máy khách
def handle_client(connection, player):
    global game_started, current_player

    if game_started:
        connection.send("Game has already started. Please try again later.".encode())
        connection.close()
        return

    connections.append(connection)
    connection.send("Welcome to the Caro game server!".encode())

    if len(connections) == 2:
        for conn in connections:
            conn.send("Both players are connected. Game is starting.".encode())

        game_thread(connection, player)
    else:
        connection.send("Waiting for another player to join...".encode())

# Vòng lặp chính của máy chủ để chấp nhận kết nối từ máy khách
while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Xác định lượt của người chơi (X hoặc O)
    player = 'X' if len(connections) % 2 == 0 else 'O'
    
    client_thread = threading.Thread(target=handle_client, args=(conn, player))
    client_thread.start()
