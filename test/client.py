import pygame
import socket
import sys
import threading

# Khởi tạo Pygame
pygame.init()

# Kích thước bảng Caro (số ô theo hàng và cột)
ROWS = 15
COLS = 15

# Kích thước mỗi ô trong bảng
CELL_SIZE = 40

# Màu sắc
BACKGROUND_COLOR = (255, 255, 255)  # Nền trắng
LINE_COLOR = (0, 0, 0)  # Đường kẻ đen
PLAYER_X_COLOR = (64, 66, 88)  # X màu đen
PLAYER_O_COLOR = (251, 161, 183)  # O màu trắng
WINNER_COLOR = (255, 0, 0)  # Màu đỏ cho người thắng
DRAW_COLOR = (0, 0, 0)  # Màu đen cho trò chơi hòa
TEXT_COLOR = (0, 0, 0)  # Màu đen cho văn bản
TEXT_COLOR2 = (255, 255, 255)  # Màu đen cho văn bản

# Khởi tạo cửa sổ Pygame
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Bảng lưu trạng thái của bàn cờ
board = [['' for _ in range(COLS)] for _ in range(ROWS)]

# Lượt của người chơi (ban đầu là X)
current_player = 'X'

# Khởi tạo kết nối socket
HOST = '127.0.0.1'  # Địa chỉ IP hoặc tên máy chủ
PORT = 12345  # Cổng kết nối
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến máy chủ
client_socket.connect((HOST, PORT))

# Hàm gửi nước đi đến máy chủ
def send_move(row, col):
    move = f"{row},{col}"
    client_socket.send(move.encode())

# Hàm nhận nước đi từ máy chủ
def receive_move():
    global game_over
    while True:
        data = client_socket.recv(1024).decode()
        if data:
            if data == "Both players are connected. Game is starting.":
                print(data)
                break
            else:
                print(data)


# Hàm vẽ bảng Caro
def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if board[row][col] == 'X':
                pygame.draw.line(screen, PLAYER_X_COLOR, (col * CELL_SIZE + 10, row * CELL_SIZE + 10), (col * CELL_SIZE + CELL_SIZE - 10, row * CELL_SIZE + CELL_SIZE - 10), 2)
                pygame.draw.line(screen, PLAYER_X_COLOR, (col * CELL_SIZE + 10, row * CELL_SIZE + CELL_SIZE - 10), (col * CELL_SIZE + CELL_SIZE - 10, row * CELL_SIZE + 10), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, PLAYER_O_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 10)

# Hàm kiểm tra chiến thắng
def check_winner(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 4 hướng kiểm tra
    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == current_player:
                count += 1
            else:
                break
        for i in range(1, 5):
            r, c = row - i * dr, col - i * dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == current_player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# Hàm kiểm tra hòa cờ (đã đầy bàn cờ và không có người thắng)
def check_draw():
    return all(board[i][j] != '' for i in range(ROWS) for j in range(COLS)) and not check_winner

# Hàm reset trò chơi
def reset_game():
    global board, current_player
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 'X'

# Hàm hiển thị thông báo
def display_message(message):
    font = pygame.font.Font(None, 48)
    text = font.render(message, True, TEXT_COLOR2)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Hàm vẽ nút chơi lại
def draw_reset_button():
    reset_font = pygame.font.Font(None, 32)
    reset_text = reset_font.render("Play Again", True, TEXT_COLOR2)
    reset_rect = reset_text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    pygame.draw.rect(screen, DRAW_COLOR, reset_rect)
    screen.blit(reset_text, reset_rect)
    return reset_rect

# Biến trạng thái trò chơi
game_over = False

# Nhận thông báo chào mừng từ máy chủ
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# Nhận thông báo bắt đầu trò chơi từ máy chủ
start_message = client_socket.recv(1024).decode()
print(start_message)

# Hàm xử lý trò chơi
def game_loop():
    global game_over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    x, y = event.pos
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == '':
                        board[row][col] = current_player
                        send_move(row, col)
                        if check_winner(row, col):
                            display_message(f"Player {current_player} wins!")
                            game_over = True
                        elif check_draw():
                            display_message("It's a draw!")
                            game_over = True
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'

        draw_board()
        if game_over:
            reset_rect = draw_reset_button()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and reset_rect.collidepoint(event.pos):
                    reset_game()
                    game_over = False

# Tạo một luồng riêng để xử lý trò chơi
game_thread = threading.Thread(target=game_loop)
game_thread.start()

# Vòng lặp chính để vẽ giao diện và nhận nước đi từ máy chủ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not game_over:
        received_move = receive_move()
        if received_move is not None:
            row, col = received_move
            board[row][col] = 'O'
            if check_winner(row, col):
                display_message(f"Player {current_player} wins!")
                game_over = True
            elif check_draw():
                display_message("It's a draw!")
                game_over = True
            else:
                current_player = 'X' if current_player == 'O' else 'O'
    
    draw_board()
    pygame.display.update()
