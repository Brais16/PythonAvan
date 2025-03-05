import pygame
import sys
import random

# Inicialitzem Pygame
pygame.init()

# Configuració del joc
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
MENU_COLOR = (50, 200, 150)
TEXT_COLOR = (0, 0, 0)

# Crear finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tres en Ratlla')
screen.fill(BG_COLOR)

# Fonts
font = pygame.font.Font(None, 36)

# Tauler
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Funcions del joc
def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * row), (WIDTH, SQUARE_SIZE * row), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * col, 0), (SQUARE_SIZE * col, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0

def is_full():
    for row in board:
        if 0 in row:
            return False
    return True

def computer_move():
    empty_cells = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

def draw_menu():
    screen.fill(MENU_COLOR)
    title_text = font.render('Tres en Ratlla', True, TEXT_COLOR)
    play_ai_text = font.render('1. Contra la màquina', True, TEXT_COLOR)
    play_pvp_text = font.render('2. Dos jugadors', True, TEXT_COLOR)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    screen.blit(play_ai_text, (WIDTH // 2 - play_ai_text.get_width() // 2, 120))
    screen.blit(play_pvp_text, (WIDTH // 2 - play_pvp_text.get_width() // 2, 170))
    pygame.display.update()

def main():
    global board
    draw_menu()

    mode = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 'ai'
                    running = False
                elif event.key == pygame.K_2:
                    mode = 'pvp'
                    running = False

    # Reiniciem el tauler
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and mode == 'pvp' and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE

                if board[mouseY][mouseX] == 0:
                    board[mouseY][mouseX] = player
                    winner = check_winner()
                    if winner != 0:
                        print(f'Jugador {winner} ha guanyat!')
                        game_over = True
                    elif is_full():
                        print('Empat!')
                        game_over = True
                    player = 2 if player == 1 else 1

            if not game_over and mode == 'ai' and player == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE

                if board[mouseY][mouseX] == 0:
                    board[mouseY][mouseX] = player
                    winner = check_winner()
                    if winner != 0:
                        print(f'Jugador {winner} ha guanyat!')
                        game_over = True
                    elif is_full():
                        print('Empat!')
                        game_over = True
                    player = 2

            if not game_over and mode == 'ai' and player == 2:
                computer_move()
                winner = check_winner()
                if winner != 0:
                    print(f'Jugador {winner} ha guanyat!')
                    game_over = True
                elif is_full():
                    print('Empat!')
                    game_over = True
                player = 1

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        pygame.display.update()

if __name__ == "__main__":
    main()
