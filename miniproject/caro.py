import pygame
import sys

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

# Hàm vẽ nút chơi lại
def draw_reset_button():
    reset_font = pygame.font.Font(None, 32)
    reset_text = reset_font.render("Play Again", True, TEXT_COLOR2)
    reset_rect = reset_text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    pygame.draw.rect(screen, DRAW_COLOR, reset_rect)
    screen.blit(reset_text, reset_rect)
    return reset_rect

# Hàm hiển thị thông báo
def display_message(winner):
    # Tạo một khung nền đen semi-transparent
    background = pygame.Surface(screen.get_size())
    background.set_alpha(128)  # Độ mờ của khung nền
    background.fill((0, 0, 0))  # Màu đen

    # Vẽ khung nền lên màn hình
    screen.blit(background, (0, 0))

    font = pygame.font.Font(None, 48)
    if winner == 'X':
        message = "Player X wins!"
        text_color = PLAYER_X_COLOR
    elif winner == 'O':
        message = "Player O wins!"
        text_color = PLAYER_O_COLOR
    else:
        message = "It's a draw!"
        text_color = TEXT_COLOR2

    text = font.render(message, True, text_color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, text_rect)



# Biến trạng thái trò chơi
game_over = False

# Vòng lặp chính
running = True
reset_rect = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if reset_rect and reset_rect.collidepoint(x, y):
                # Reset lại game
                reset_game()
                game_over = False
            elif not game_over:
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == '':
                    board[row][col] = current_player
                    if check_winner(row, col):
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
    pygame.display.update()

pygame.quit()
sys.exit()
