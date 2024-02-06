# For Generating Cycle Moves
# Source : ChatGPT

import math

radius = 50  # Radius of the circle
num_edges = 1000  # Number of edges

commands = []
for i in range(num_edges):
    angle = 2 * math.pi * i / num_edges  # Calculate the angle for each edge
    dx = radius * math.cos(angle)  # Calculate the x-coordinate
    dy = radius * math.sin(angle)  # Calculate the y-coordinate

    # Convert coordinates to the nearest cardinal direction
    if dx > 0:
        direction_x = "E"
    elif dx < 0:
        direction_x = "W"
    else:
        direction_x = "N"
    if dy > 0:
        direction_y = "N"
    elif dy < 0:
        direction_y = "S"
    else:
        direction_y = "W"

    # Append commands to move the person
    commands.append(f"1 {direction_x}")
    commands.append(f"1 {direction_y}")

# Save commands to a file
with open("circle_moves.txt", "w") as file:
    file.write("\n".join(commands))
