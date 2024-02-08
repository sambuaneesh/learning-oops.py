import pygame

prefix = "kaooa_package/assets/"
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

crow_text = font.render("Crows Turn", True, (255, 255, 255))
crow_text_base = font_base.render("Crows Turn", True, (0, 0, 0))

vulture_text = font.render("Vulture Turn", True, (255, 255, 255))
vulture_text_base = font_base.render("Vulture Turn", True, (0, 0, 0))

crow_win = pygame.font.Font(None, 100).render("Crows Win", True, (255, 255, 255))
vulture_win = pygame.font.Font(None, 100).render("Vulture Wins", True, (255, 255, 255))
