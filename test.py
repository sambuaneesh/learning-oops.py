import pygame
from sys import exit

prefix = "kaooa_package/assets/"
WIDTH, HEIGHT = 800, 800
BOARD_OFFSET_X = (WIDTH - 800) // 2
BOARD_OFFSET_Y = (HEIGHT - 800) // 2
PLACE_HOLDERS = [(398, 87), (100, 291), (321, 298), (478, 298), (696, 292), (277, 416), (522, 416), (399, 497), (191, 623), (602, 619)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaooa Game")
clock = pygame.time.Clock()
board_image = pygame.image.load(prefix + "board.png").convert_alpha()
crow_image = pygame.image.load(prefix + "crow.png").convert_alpha()
vulture_image = pygame.image.load(prefix + "vulture.png").convert_alpha()
captured_crows = 0
player = 0

font_base = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 50)
# xl_font_base = pygame.font.Font(None, 50)
# xl_font = pygame.font.Font(None, 50)
crow_text = font.render("Crows Turn", True, (255, 255, 255))
crow_text_base = font_base.render("Crows Turn", True, (0,0,0))
vulture_text = font.render("Vulture Turn", True, (255, 255, 255))
vulture_text_base = font_base.render("Vulture Turn", True, (0,0,0))
crow_win = pygame.font.Font(None, 100).render("Crows Win", True, (255, 255, 255))
vulture_win = pygame.font.Font(None, 100).render("Vulture Wins", True, (255, 255, 255))

class GamePiece:
    def __init__(self, piece_type, position):
        self.piece_type = piece_type  # 0 for crow, 1 for vulture
        self.position = position

    def move(self, new_position):
        self.position = new_position

class GameBoard:
    def __init__(self):
        self.pieces = []
        self.adjacent_positions = {
            PLACE_HOLDERS[0]: [PLACE_HOLDERS[2], PLACE_HOLDERS[3]],
            PLACE_HOLDERS[1]: [PLACE_HOLDERS[2], PLACE_HOLDERS[5]],
            PLACE_HOLDERS[2]: [PLACE_HOLDERS[0], PLACE_HOLDERS[1], PLACE_HOLDERS[3], PLACE_HOLDERS[5]],
            PLACE_HOLDERS[3]: [PLACE_HOLDERS[0], PLACE_HOLDERS[2], PLACE_HOLDERS[4], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[4]: [PLACE_HOLDERS[3], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[5]: [PLACE_HOLDERS[1], PLACE_HOLDERS[2], PLACE_HOLDERS[7], PLACE_HOLDERS[8]],
            PLACE_HOLDERS[6]: [PLACE_HOLDERS[3], PLACE_HOLDERS[4], PLACE_HOLDERS[7], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[7]: [PLACE_HOLDERS[5], PLACE_HOLDERS[6], PLACE_HOLDERS[8], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[8]: [PLACE_HOLDERS[5], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[9]: [PLACE_HOLDERS[6], PLACE_HOLDERS[7]],
        }
        self.jumping_positions = {
            PLACE_HOLDERS[0]: [PLACE_HOLDERS[5], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[1]: [PLACE_HOLDERS[3], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[2]: [PLACE_HOLDERS[4], PLACE_HOLDERS[8]],
            PLACE_HOLDERS[3]: [PLACE_HOLDERS[1], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[4]: [PLACE_HOLDERS[2], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[5]: [PLACE_HOLDERS[0], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[6]: [PLACE_HOLDERS[8], PLACE_HOLDERS[0]],
            PLACE_HOLDERS[7]: [PLACE_HOLDERS[1], PLACE_HOLDERS[4]],
            PLACE_HOLDERS[8]: [PLACE_HOLDERS[2], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[9]: [PLACE_HOLDERS[3], PLACE_HOLDERS[5]],
        }
        self.selected_piece = None

    def get_adjacent_positions(self, position):
        return self.adjacent_positions[position]

    def is_jump_valid(self, pos1, pos2):
        return pos2 in self.jumping_positions[pos1]

    def add_piece(self, piece):
        self.pieces.append(piece)

    def is_move_valid(self, piece, new_position):
        global captured_crows
        # Check if new_position is within the placeholders
        if new_position not in PLACE_HOLDERS:
            return False

        # check if new_position is occupied
        if new_position in [p.position for p in self.pieces]:
            return False

        # For crows, check if the new position is adjacent
        if piece.piece_type == 0:  # Crow
            current_index = PLACE_HOLDERS.index(piece.position)
            new_index = PLACE_HOLDERS.index(new_position)
            # Define adjacency based on your game's logic, this is a placeholder
            if new_index in self.adjacent_positions[current_index]:
                return True
            return False

        # For the vulture, check if it's either an adjacent move or a valid jump
        elif piece.piece_type == 1:  # Vulture
            # Adjacent move check (similar to crows)
            if new_position in self.get_adjacent_positions(piece.position):
                return True
            # Jump check
            else:
                if self.is_jump_valid(piece.position, new_position):
                    # check if there is a crow adjacent to piece.position and new_position
                    for p in self.pieces:
                        adj1 = self.get_adjacent_positions(piece.position)
                        adj2 = self.get_adjacent_positions(new_position)
                        if p.position in adj1 and p.position in adj2 and p.piece_type == 0:
                            self.pieces.remove(p)
                            captured_crows += 1
                            return True                                                        
                    return False
            return False
        

    def is_vulture_trapped(self):
        vulture_piece = next((p for p in self.pieces if p.piece_type == 1), None)
        if not vulture_piece:
            return False  # No vulture found, should not happen
        adjacent_positions = self.get_adjacent_positions(vulture_piece.position)
        for pos in adjacent_positions:
            if self.is_move_valid(vulture_piece, pos):
                return False  # Found a valid move
        return True  # No valid moves found

    def is_win_condition_met(self):
        if captured_crows >= 4:
            return 1  # Vulture wins
        if self.is_vulture_trapped():
            return 0  # Crows win
        
        return -1  # No win yet

class Game:
    def __init__(self):
        self.board = GameBoard()
        self.turn = 0  # 0 for crows, 1 for vulture
        self.crows_left = 7
        self.vulture_placed = False

    def is_occupied(self, position):
        return position in [p.position for p in self.board.pieces]

    def place_piece(self, position):
        if self.is_occupied(position):
            return
        if self.turn == 0 and self.crows_left > 0:
            self.board.add_piece(GamePiece(0, position))
            self.crows_left -= 1
        elif self.turn == 1 and not self.vulture_placed:
            self.board.add_piece(GamePiece(1, position))
            self.vulture_placed = True
        self.turn = (self.turn + 1) % 2

    def move_piece(self, piece, new_position):
        if game.turn == 1 and self.board.is_move_valid(piece, new_position):
            if piece.piece_type == 1:  # Vulture
                piece.move(new_position)
                self.turn ^= 1
                self.update_game()
                return True
        elif self.board.is_move_valid(piece, new_position):
            if piece.piece_type == 0:
                piece.move(new_position)
                self.turn ^= 1
                self.update_game()
                return True
        return False

    def update_game(self):
        win_condition = self.board.is_win_condition_met()
        # if win_condition != -1:
        #     # Implement game over logic, display winner, etc.
        #     # print("Game Over. Winner is", "Crows" if win_condition == 0 else "Vulture")
        return win_condition

# Initialize game
game = Game()

def get_near(x, y):
    for pos in PLACE_HOLDERS:
        if ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5 < 50:
            return pos
    return None

def blit_image(image, x, y):
    screen.blit(image, (x - 75, y - 75))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            coord = get_near(x, y)
            if(game.turn == 0 and game.crows_left > 0):
                if coord:
                    game.place_piece(coord)
            elif game.turn == 1 and not game.vulture_placed:
                coord = get_near(x, y)
                if coord:
                    game.place_piece(coord)
            elif game.turn == 1:
                selected_piece = next((p for p in game.board.pieces if p.piece_type == 1), None)
                if selected_piece:
                    if coord:
                        game.move_piece(selected_piece, coord)
            elif game.turn == 0 and not selected_piece and coord and game.crows_left == 0:
                # selected piece = piece at coord
                print(1)
                game.board.selected_piece = next((p for p in game.board.pieces if p.position == coord), None)
            elif game.turn == 0 and selected_piece and coord:
                game.move_piece(selected_piece, coord)
                game.board.selected_piece = None
            print(game.board.selected_piece)
            
    screen.blit(board_image, (BOARD_OFFSET_X, BOARD_OFFSET_Y))
    for i in PLACE_HOLDERS:
        pygame.draw.circle(screen, (255, 255, 255), i, 25, 5)
    if game.turn == 0:
        screen.blit(crow_text_base, (8, 15))
        screen.blit(crow_text, (10, 10))
    else:
        screen.blit(vulture_text_base, (8, 15))
        screen.blit(vulture_text, (10, 10))
    for piece in game.board.pieces:
        img = crow_image if piece.piece_type == 0 else vulture_image
        blit_image(img, *piece.position)
    if game.board.selected_piece:
        # highlight the selected piece
        pygame.draw.circle(screen, (0, 255, 0), game.board.selected_piece.position, 50, 5)
    win_condition = game.update_game()
    if win_condition != -1:
        print(win_condition)
        screen.fill((0, 0, 0))
        if win_condition == 0:
            blit_image(crow_image, BOARD_OFFSET_X + 120, HEIGHT//2 + 25)
            screen.blit(crow_win, (BOARD_OFFSET_X + 175, HEIGHT//2))
        else:
            blit_image(vulture_image, BOARD_OFFSET_X + 120, HEIGHT//2 + 25)
            screen.blit(vulture_win, (BOARD_OFFSET_X + 175, HEIGHT//2))

    pygame.display.update()
    clock.tick(60)

