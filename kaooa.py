import pygame
from sys import exit

prefix = "kaooa_package/assets/"

WIDTH, HEIGHT = 800,800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaooa Game")
clock = pygame.time.Clock()

boardimage = pygame.image.load(prefix+"board.png").convert_alpha()
crow_image = pygame.image.load(prefix+"crow.png").convert_alpha()
vulture_image = pygame.image.load(prefix+"vulture.png").convert_alpha()

BOARD_OFFSET_X = (WIDTH - boardimage.get_width()) // 2
BOARD_OFFSET_Y = (HEIGHT - boardimage.get_height()) // 2

place_holders = [(398, 87), (100, 291), (321, 298), (478, 298), (696, 292), (277, 416), (522, 416), (399, 497), (191, 623), (602, 619)]


def get_near(x, y):
    for i in range(len(place_holders)):
        if ((place_holders[i][0]-x)**2 + (place_holders[i][1]-y)**2)**0.5 < 50:
            return place_holders[i]
    return -1

def blit_image(image, x, y):
    screen.blit(image, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(get_near(x, y))
    screen.blit(boardimage, (BOARD_OFFSET_X, BOARD_OFFSET_Y))
    for i in place_holders:
        pygame.draw.circle(screen, (255, 255, 255), i, 25, 3)
    
    pygame.display.update()
    clock.tick(60)
