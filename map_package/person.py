import math


class Person:
    def __init__(self):
        self.x = [0]
        self.y = [0]

    def move(self, distance, direction):
        move_x, move_y = 0, 0
        if direction == "N":
            move_y = distance
        elif direction == "S":
            move_y = -distance
        elif direction == "E":
            move_x = distance
        elif direction == "W":
            move_x = -distance
        elif direction == "NE":
            angle = math.pi / 4
            move_x = distance * math.cos(angle)
            move_y = distance * math.sin(angle)
        elif direction == "SE":
            angle = -math.pi / 4
            move_x = distance * math.cos(angle)
            move_y = distance * math.sin(angle)
        elif direction == "NW":
            angle = 3 * math.pi / 4
            move_x = distance * math.cos(angle)
            move_y = distance * math.sin(angle)
        elif direction == "SW":
            angle = -3 * math.pi / 4
            move_x = distance * math.cos(angle)
            move_y = distance * math.sin(angle)
        else:
            raise ValueError("Invalid direction.")

        last_x = self.x[-1]
        last_y = self.y[-1]
        self.x.append(last_x + move_x)
        self.y.append(last_y + move_y)
