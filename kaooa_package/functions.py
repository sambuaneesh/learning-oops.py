from kaooa_package.definitions import *

def get_near(x, y):
    for pos in PLACE_HOLDERS:
        if ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5 < 50:
            return pos
    return None

def blit_image(image, x, y):
    screen.blit(image, (x - 75, y - 75))
