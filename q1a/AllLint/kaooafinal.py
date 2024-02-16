"""Module for the Kaooa game."""

import sys
import pygame

# Globals

SCREEN = None
CLOCK = None

BOARD_IMAGE = None
CROW_IMAGE = None
VULTURE_IMAGE = None

PLAYER = 0

FONT_BASE = None
FONT = None

CROW_TEXT = None
CROW_TEXT_BASE = None

VULTURE_TEXT = None
VULTURE_TEXT_BASE = None

CROW_WIN = None
VULTURE_WIN = None


class Game:
    """Class representing the main game logic."""

    def __init__(self):
        self.board = GameBoard()
        self.turn = 0  # 0 = crows 1 = vulture
        self.crows_left = 7
        self.vulture_placed = False

    def is_occupied(self, position):
        """Check if a position is occupied by a piece."""
        return position in [p.position for p in self.board.pieces]

    def place_piece(self, position):
        """Place a piece on the board."""
        if self.is_occupied(position):
            return
        if self.turn == 0 and self.crows_left > 0:
            self.board.add_piece(GamePiece(0, position))
            self.crows_left -= 1
        elif self.turn == 1 and not self.vulture_placed:
            self.board.add_piece(GamePiece(1, position))
            self.vulture_placed = True
        self.turn ^= 1

    def move_piece(self, piece, new_position):
        """Move a piece to a new position."""
        if self.turn == 1 and self.board.is_move_valid(piece, new_position):
            if piece.piece_type == 1:
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
        """Update the game state."""
        win_condition = self.board.is_win_condition_met()
        return win_condition


class GamePiece:
    """Class representing a game piece."""

    def __init__(self, piece_type, position):
        self.piece_type = piece_type
        self.position = position

    def move(self, new_position):
        """Move the piece to a new position."""
        self.position = new_position

    def __repr__(self):
        return f"Piece {self.piece_type} at {self.position}"


class GameBoard:
    """Class representing the game board."""

    def __init__(self):
        self.pieces = []
        self.adjacent_positions = {
            PLACE_HOLDERS[0]: [PLACE_HOLDERS[2], PLACE_HOLDERS[3]],
            PLACE_HOLDERS[1]: [PLACE_HOLDERS[2], PLACE_HOLDERS[5]],
            PLACE_HOLDERS[2]: [
                PLACE_HOLDERS[0],
                PLACE_HOLDERS[1],
                PLACE_HOLDERS[3],
                PLACE_HOLDERS[5],
            ],
            PLACE_HOLDERS[3]: [
                PLACE_HOLDERS[0],
                PLACE_HOLDERS[2],
                PLACE_HOLDERS[4],
                PLACE_HOLDERS[6],
            ],
            PLACE_HOLDERS[4]: [PLACE_HOLDERS[3], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[5]: [
                PLACE_HOLDERS[1],
                PLACE_HOLDERS[2],
                PLACE_HOLDERS[7],
                PLACE_HOLDERS[8],
            ],
            PLACE_HOLDERS[6]: [
                PLACE_HOLDERS[3],
                PLACE_HOLDERS[4],
                PLACE_HOLDERS[7],
                PLACE_HOLDERS[9],
            ],
            PLACE_HOLDERS[7]: [
                PLACE_HOLDERS[5],
                PLACE_HOLDERS[6],
                PLACE_HOLDERS[8],
                PLACE_HOLDERS[9],
            ],
            PLACE_HOLDERS[8]: [PLACE_HOLDERS[5], PLACE_HOLDERS[7]],
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
        self.occupied_positions = []
        self.captured_crows = 0

    def get_adjacent_positions(self, position):
        """Get the adjacent positions of a given position."""
        return self.adjacent_positions[position]

    def is_jump_valid(self, pos1, pos2):
        """Check if a jump is valid."""
        return pos2 in self.jumping_positions[pos1]

    def add_piece(self, piece):
        """Add a piece to the board."""
        self.pieces.append(piece)

    def remove_piece(self, piece):
        """Remove a piece from the board."""
        self.pieces.remove(piece)

    def is_move_valid(self, piece, new_position):
        """Check if a move is valid."""
        if new_position not in PLACE_HOLDERS:
            return False

        if new_position in [p.position for p in self.pieces]:
            return False

        if piece.piece_type == 0:
            return new_position in self.get_adjacent_positions(piece.position)

        if piece.piece_type == 1:
            if new_position in self.get_adjacent_positions(piece.position):
                return True
            if self.is_jump_valid(piece.position, new_position):
                adj1 = self.get_adjacent_positions(piece.position)
                adj2 = self.get_adjacent_positions(new_position)
                for p in self.pieces:
                    if p.position in adj1 and p.position in adj2 and p.piece_type == 0:
                        self.pieces.remove(p)
                        self.captured_crows += 1
                        return True
        return False

    def is_vulture_trapped(self):
        """Check if the vulture is trapped."""
        vulture_piece = next((p for p in self.pieces if p.piece_type == 1), None)
        if not vulture_piece:
            return False
        available_positions = []
        adjacent_positions = self.get_adjacent_positions(vulture_piece.position)
        jump_positions = self.jumping_positions[vulture_piece.position]
        available_positions.extend(adjacent_positions)
        available_positions.extend(jump_positions)
        for pos in available_positions:
            if pos not in [p.position for p in self.pieces]:
                return False  # Vulture has at least one valid move
        return True  # No valid moves found

    def is_win_condition_met(self):
        """Check if the win condition is met."""
        if self.captured_crows >= 4:
            return 1
        if self.is_vulture_trapped():
            return 0
        return -1


def get_near(x_cor, y_cor):
    """Get the nearest placeholder to a given position."""
    for pos in PLACE_HOLDERS:
        if ((pos[0] - x_cor) ** 2 + (pos[1] - y_cor) ** 2) ** 0.5 < 50:
            return pos
    return None


def blit_image(image, x_cor, y_cor):
    """Blit an image to the screen."""
    SCREEN.blit(image, (x_cor - 75, y_cor - 75))


PREFIX = "kaooa_package/assets/"
WIDTH, HEIGHT = 800, 800

PLACE_HOLDERS = [
    (398, 87),
    (100, 291),
    (321, 298),
    (478, 298),
    (696, 292),
    (277, 416),
    (522, 416),
    (399, 497),
    (191, 623),
    (602, 619),
]


def handle_mouse_click(coordinates, game_instance):
    """Handle mouse click."""
    if game_instance.turn == 0:
        handle_crows_turn(coordinates, game_instance)
    else:
        handle_vulture_turn(coordinates, game_instance)


def handle_crows_turn(coordinates, game_instance):
    """Handle crows turn."""
    if game_instance.crows_left > 0:
        game_instance.place_piece(coordinates)
    elif not game_instance.board.selected_piece and game_instance.turn == 0:
        handle_crow_selection(coordinates, game_instance)
    else:
        handle_piece_move(
            game_instance.board.selected_piece, coordinates, game_instance
        )


def handle_crow_selection(coordinates, game_instance):
    """Handle crow selection."""
    piece = next(
        (p for p in game_instance.board.pieces if p.position == coordinates), None
    )
    if piece and piece.piece_type == 0:
        adjacent_positions = game_instance.board.get_adjacent_positions(piece.position)
        occupied = sum(
            1 for position in adjacent_positions if game_instance.is_occupied(position)
        )
        if len(adjacent_positions) - occupied > 0:
            game_instance.board.selected_piece = piece
        else:
            game_instance.board.selected_piece = None
    else:
        game_instance.board.selected_piece = None


def handle_vulture_turn(coordinates, game_instance):
    """Handle vulture turn."""
    if not game_instance.vulture_placed:
        game_instance.place_piece(coordinates)
    else:
        vulture = next(
            (p for p in game_instance.board.pieces if p.piece_type == 1), None
        )
        if vulture:
            handle_piece_move(vulture, coordinates, game_instance)


def handle_piece_move(piece, coordinates, game_instance):
    """Handle piece move."""
    if game_instance.move_piece(piece, coordinates):
        game_instance.board.selected_piece = None


def render_game_screen(game_instance):
    """Render the game screen."""
    SCREEN.blit(BOARD_IMAGE, (0, 0))
    render_place_holders(game_instance)
    render_turn_indicator(game_instance)
    render_game_pieces(game_instance)
    render_selected_piece(game_instance)
    render_win_condition(game_instance)


def render_place_holders(game_inst):
    """Render the place holders."""
    for i in PLACE_HOLDERS:
        if (
            game_inst.crows_left > 0
            and game_inst.turn == 0
            or not game_inst.vulture_placed
        ):
            pygame.draw.circle(SCREEN, (0, 255, 0), i, 25, 5)
        else:
            pygame.draw.circle(SCREEN, (255, 255, 255), i, 25, 5)


def render_turn_indicator(game_instance):
    """Render the turn indicator."""
    if game_instance.turn == 0:
        SCREEN.blit(CROW_TEXT_BASE, (8, 15))
        SCREEN.blit(CROW_TEXT, (10, 10))
        highlight_crows(game_instance)
    else:
        SCREEN.blit(VULTURE_TEXT_BASE, (8, 15))
        SCREEN.blit(VULTURE_TEXT, (10, 10))
        highlight_vulture(game_instance)


def highlight_crows(game_instance):
    """Highlight crows."""
    if not game_instance.board.selected_piece and game_instance.crows_left == 0:
        for piece in game_instance.board.pieces:
            if piece.piece_type == 0:
                pygame.draw.circle(SCREEN, (143, 0, 255), piece.position, 47, 7)


def highlight_vulture(game_instance):
    """Highlight vulture."""
    vulture = next((p for p in game_instance.board.pieces if p.piece_type == 1), None)
    if vulture:
        pygame.draw.circle(SCREEN, (0, 255, 0), vulture.position, 50, 5)


def render_game_pieces(game_instance):
    """Render the game pieces."""
    for piece in game_instance.board.pieces:
        img = CROW_IMAGE if piece.piece_type == 0 else VULTURE_IMAGE
        blit_image(img, *piece.position)


def render_selected_piece(game_instance):
    """Render the selected piece."""
    if game_instance.board.selected_piece:
        pygame.draw.circle(
            SCREEN, (0, 255, 0), game_instance.board.selected_piece.position, 47, 5
        )


def render_win_condition(game_instance):
    """Render the win condition."""
    win_condition = game_instance.update_game()
    if win_condition != -1:
        SCREEN.fill((0, 0, 0))
        if win_condition == 0:
            blit_image(CROW_IMAGE, 120, HEIGHT // 2 + 25)
            SCREEN.blit(CROW_WIN, (175, HEIGHT // 2))
        else:
            blit_image(VULTURE_IMAGE, 120, HEIGHT // 2 + 25)
            SCREEN.blit(VULTURE_WIN, (175, HEIGHT // 2))


if __name__ == "__main__":
    pygame.init()
    game = Game()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kaooa Game")
    CLOCK = pygame.time.Clock()

    BOARD_IMAGE = pygame.image.load(PREFIX + "board.png").convert_alpha()
    CROW_IMAGE = pygame.image.load(PREFIX + "crow.png").convert_alpha()
    VULTURE_IMAGE = pygame.image.load(PREFIX + "vulture.png").convert_alpha()

    PLAYER = 0

    FONT_BASE = pygame.font.Font(None, 50)
    FONT = pygame.font.Font(None, 50)

    CROW_TEXT = FONT.render("Crows Turn", True, (255, 255, 255))
    CROW_TEXT_BASE = FONT_BASE.render("Crows Turn", True, (0, 0, 0))

    VULTURE_TEXT = FONT.render("Vulture Turn", True, (255, 255, 255))
    VULTURE_TEXT_BASE = FONT_BASE.render("Vulture Turn", True, (0, 0, 0))

    CROW_WIN = pygame.font.Font(None, 100).render("Crows Win", True, (255, 255, 255))
    VULTURE_WIN = pygame.font.Font(None, 100).render(
        "Vulture Wins", True, (255, 255, 255)
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                coord = get_near(x, y)
                if coord:
                    handle_mouse_click(coord, game)

        render_game_screen(game)
        pygame.display.update()
        CLOCK.tick(10)
