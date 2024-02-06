import sys
import time
from map_package.person import Person
from map_package.movement_parser import parse_distance
from map_package.plotter import plot_movement
from common.clear import clear


def main():
    person = Person()

    # checkin if cmd arguments are there
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, "r") as file:
                for line in file:
                    try:
                        distance_str, direction = line.strip().split()
                        distance = parse_distance(distance_str)
                        print(f"Moving {distance}cm {direction}")
                        time.sleep(0.01)
                        person.move(distance, direction)
                    except ValueError as e:
                        print(e)
                        print("skipping line:", line.strip())
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return
    else:
        print(
            "Enter distance and direction (e.g., '3mm N', '4cm NW', '2 SE'), or press Enter to exit:"
        )
        while True:
            usr_input = input()
            if not usr_input:
                break
            try:
                distance_str, direction = usr_input.split()
                distance = parse_distance(distance_str)
                person.move(distance, direction)
            except ValueError as e:
                print(e)
                print(
                    "Invalid input format. Please enter distance and direction separated by a space."
                )

    plot_movement(person.x, person.y)


if __name__ == "__main__":
    main()
    clear()
