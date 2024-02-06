2D Person Movement Plotter README

This program allows you to plot the movement of a person in a 2D world based on a sequence of input commands.

Features:

- Supports movement in four cardinal directions (N, S, E, W) and four diagonal directions (NE, NW, SE, SW).
- Supports distances in both millimeters (mm) and centimeters (cm).
- Accepts input from the command line or from a file.
- Error handling for invalid input formats and missing files.
- Interactive plotting with Matplotlib.

Usage:

1. Run the program from the command line:

   python person_movement_plotter.py [input_file.txt]

   If an input file is provided, the program reads commands from the file. Each line in the file should contain a distance and direction separated by a space.

   Example input file (input.txt):

   ```
   3mm N
   4cm NW
   2 SE
   ```

   If no input file is provided, the program prompts you to enter commands interactively.

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

Note:

- If the measurement unit (mm or cm) is not provided, the default unit assumed is millimeters.
- Invalid input lines or commands will be skipped, and an error message will be displayed.
- The program uses interactive plotting, allowing you to zoom, pan, and save the plot as an image file.
