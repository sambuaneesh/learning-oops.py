import pygame
from sys import exit

prefix = "kaooa_package/assets/"
WIDTH, HEIGHT = 800, 800
BOARD_OFFSET_X = (WIDTH - 800) // 2
BOARD_OFFSET_Y = (HEIGHT - 800) // 2
PLACE_HOLDERS = [(398, 87), (100, 291), (321, 298), (478, 298), (696, 292), (277, 416), (522, 416), (399, 497), (191, 623), (602, 619)]
CROW = 0
VULTURE = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaooa Game")
clock = pygame.time.Clock()
board_image = pygame.image.load(prefix + "board.png").convert_alpha()
crow_image = pygame.image.load(prefix + "crow.png").convert_alpha()
vulture_image = pygame.image.load(prefix + "vulture.png").convert_alpha()

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

class Crow(GamePiece):
    def __init__(self, position):
        super().__init__(0, position)

class Vulture(GamePiece):
    def __init__(self, position):
        super().__init__(1, position)

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

class Game:
    def __init__(self):
        self.board = GameBoard()
        self.turn = CROW
        self.crows_left = 7
        self.vulture_placed = False
        self.captured_crows = 0

def get_near(x, y):
    for pos in PLACE_HOLDERS:
        if ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5 < 50:
            return pos
    return None

def blit_image(image, x, y):
    screen.blit(image, (x - 75, y - 75))

game = Game()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.turn == CROW:
                    crows_left = game.crows_left
                elif game.turn == VULTURE:
                    print("Vulture turn")
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
