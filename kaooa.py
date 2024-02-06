import turtle


def circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def get_mouse_click_coord(x, y):
    print("Clicked at:", x, y)


# Function to exit the game
def exit_game():
    turtle.bye()


coords = [
    [0, 397],
    [-381, 138],
    [-98, 129],
    [100, 128],
    [382, 135],
    [-158, -20],
    [158, -21],
    [0, -127],
    [-266, -292],
    [271, -289],
]

screen = turtle.Screen()
screen.setup(900, 900)
# get bg image
screen.bgpic("kaooa_package/assets/board.png")
screen.title("Kaooa")
# screen.onscreenclick(get_mouse_click_coord)


for coord in coords:
    circle(coord[0], coord[1] - 16)

# Register exit key
screen.onkeypress(exit_game, "q")
screen.listen()

# Main loop
turtle.done()
