import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 900,900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaooa Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load assets
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "kaooa_package", "assets")
board_image = pygame.image.load(os.path.join(assets_path, "board.png")).convert_alpha()
crow_image = pygame.image.load(os.path.join(assets_path, "crow.png")).convert_alpha()
vulture_image = pygame.image.load(os.path.join(assets_path, "vulture.png")).convert_alpha()

# Define game variables
running = True
clock = pygame.time.Clock()

# Define game state variables
selected_piece = None
game_board = [
    ["", "", "", "", ""],  # Top row
    ["", "", "", "", ""],  # Left diagonal
    ["", "", "", "", ""],  # Middle row
    ["", "", "", "", ""],  # Right diagonal
    ["", "", "", "", ""],  # Bottom row
]

# Define game constants
CELL_SIZE = 100
BOARD_OFFSET_X = (WIDTH - board_image.get_width()) // 2
BOARD_OFFSET_Y = (HEIGHT - board_image.get_height()) // 2

# Function to draw the game board
def draw_board():
    screen.blit(board_image, (BOARD_OFFSET_X, BOARD_OFFSET_Y))

# Function to draw game pieces
def draw_pieces():
    for y, row in enumerate(game_board):
        for x, piece in enumerate(row):
            if piece == "crow":
                screen.blit(crow_image, (BOARD_OFFSET_X + x * CELL_SIZE, BOARD_OFFSET_Y + y * CELL_SIZE))
            elif piece == "vulture":
                screen.blit(vulture_image, (BOARD_OFFSET_X + x * CELL_SIZE, BOARD_OFFSET_Y + y * CELL_SIZE))

# Function to handle player clicks
def handle_click(pos):
    global selected_piece
    x, y = pos
    x_idx = (x - BOARD_OFFSET_X) // CELL_SIZE
    y_idx = (y - BOARD_OFFSET_Y) // CELL_SIZE
    if 0 <= x_idx < 5 and 0 <= y_idx < 5:
        if game_board[y_idx][x_idx] == "":
            game_board[y_idx][x_idx] = "crow"
            selected_piece = None
        elif selected_piece is None:
            selected_piece = (x_idx, y_idx)
        elif selected_piece == (x_idx, y_idx):
            selected_piece = None
        else:
            game_board[selected_piece[1]][selected_piece[0]] = ""
            game_board[y_idx][x_idx] = "crow"
            selected_piece = None

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_click(pygame.mouse.get_pos())

    # Clear the screen
    screen.fill(WHITE)

    # Draw the game board
    draw_board()

    # Draw the game pieces
    draw_pieces()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
