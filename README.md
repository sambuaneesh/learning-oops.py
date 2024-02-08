# Table of Contents

- [Foreword](#foreword)
- [Faculty Marks Directory](#faculty-marks-directory)
  - [Features](#features)
  - [Usage](#usage)
  - [Note](#note)
- [2D Person Movement Plotter](#2d-person-movement-plotter)
  - [Features](#features-1)
  - [Usage](#usage-1)
  - [Note](#note-1)
- [Kaooa Game](#kaooa-game)
  - [Features](#features-2)
  - [Usage](#usage-2)
  - [Note](#note-2)

# Foreword

1. **Python Installation**: Make sure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

2. **Create a Virtual Environment (Optional)**: It's a good practice to work within a virtual environment to avoid conflicts with other Python projects. You can create a virtual environment using `venv` or `virtualenv`:

   ```
   python3 -m venv myenv
   ```

   Activate the virtual environment:

   - On Windows:

     ```
     myenv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source myenv/bin/activate
     ```

3. **Install Dependencies**: Once inside the virtual environment, navigate to the project directory and install the dependencies listed in the `requirements.txt` file. Use the following command:

   ```
   pip install -r requirements.txt
   ```

   This command will install all the required packages and their specific versions specified in the `requirements.txt` file.

---

# Faculty Marks Directory

This program allows you to manage a directory of marks entries, including adding, loading from and saving to CSV files, displaying, removing, updating, and searching entries.

## Features

- Add new marks entries with various attributes such as first name, last name, roll number, course name, semester, exam type, total marks, and scored marks.
- Load entries from a CSV file and save entries to a CSV file.
- Display the marks directory in a tabular format.
- Remove entries based on a specified attribute and value.
- Update entries based on a specified attribute and value.
- Search for entries based on a specified attribute and value.
- Fuzzy search of attributes.
- If multiple entries are matched, user is given an option to choose a specific entry.

## Usage

1. Run the program from the command line:

   ```
   python mdirectory.py
   ```

2. Follow the on-screen instructions to perform various operations on the marks directory.

## Note

- When prompted for options, enter the corresponding number to perform the desired operation.
- The program provides a menu-driven interface for easy navigation and operation.
- Error messages are displayed for invalid input or missing files.

---

# 2D Person Movement Plotter

This program allows you to plot the movement of a person in a 2D world based on a sequence of input commands.

## Features

- Supports movement in four cardinal directions (N, S, E, W) and four diagonal directions (NE, NW, SE, SW).
- Supports distances in both millimeters (mm) and centimeters (cm).
- Accepts input from the command line or from a file.
- Error handling for invalid input formats and missing files.
- Interactive plotting with Matplotlib.

## Usage

1. Run the program from the command line:

   ```
   python map.py [input_file.txt]
   ```

   - If an input file is provided, the program reads commands from the file. Each line in the file should contain a distance and direction separated by a space.

   - Example input file (input.txt):

     ```
     3mm N
     4cm NW
     2 SE
     ```

   - If no input file is provided, the program prompts you to enter commands interactively.

2. Enter commands in the following format:

   - For distances in millimeters: "distance mm direction"
   - For distances in centimeters: "distance cm direction"

   Available directions: N, S, E, W, NE, NW, SE, SW

   Example commands:

   ```
   3mm N
   4cm NW
   2 SE
   ```

3. The program will plot the movement of the person in a 2D world based on the provided commands.

4. Close the plot window to exit the program.

## Note

- If the measurement unit (mm or cm) is not provided, the default unit assumed is millimeters.
- Invalid input lines or commands will be skipped, and an error message will be displayed.
- The program uses interactive plotting, allowing you to zoom, pan, and save the plot as an image file.

---

# Kaooa Game

This program implements the Kaooa game, also known as "Vulture and Crows," a traditional hunt game from India.

## Features

- Play as either the crows or the vulture.
- Place tokens on a pentagram-shaped board and move them strategically.
- Simple and intuitive controls using mouse clicks.
- Visual representation of the game board and tokens using Pygame.
- Win conditions for both the crows and the vulture.
- Interactive gameplay with real-time updates.

## Usage

1. Run the program from the command line:

   ```
   python kaooa.py
   ```

2. Click on the desired position on the game board to place a token.
3. Move the tokens strategically to outsmart your opponent.
4. The vulture must capture at least four crows to win, while the crows must trap the vulture to win.

## Note

- The program uses Pygame for graphics and event handling.
- Tokens are represented by images (crow and vulture).
- The game board is displayed on a graphical window, and tokens are placed and moved using mouse clicks.
- Win conditions are checked after each move, and the game ends when a win condition is met.
