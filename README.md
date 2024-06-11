# Rush Hour Game

## Description

This project implements a version of the Rush Hour puzzle game. The objective is to move the red car out of the traffic jam and through the exit. The game is played on a 7x7 grid, where various cars of different lengths and orientations are placed. The player moves these cars in their respective orientations to free the red car.

## Files

- `car.py`: Contains the `Car` class which represents a car in the game.
- `board.py`: Contains the `Board` class which represents the game board and manages car movements.
- `game.py`: Contains the `Game` class which manages the game logic and user interactions.
- `helper.py`: Contains utility functions, including `load_json` for loading the initial board configuration from a JSON file.
- `car_config.json`: An example JSON file that specifies the initial configuration of cars on the board.

## Classes and Functions

### `Car` Class (car.py)

Represents a car in the game.

**Attributes:**
- `name` (str): The name of the car (e.g., 'Y', 'B', 'O', 'W', 'G', 'R').
- `length` (int): The length of the car (between 2 and 4).
- `orientation` (int): The orientation of the car (0 for vertical, 1 for horizontal).
- `location` (tuple): The (row, col) coordinate of the car's minimum location (closest to the top-left corner).

**Methods:**
- `__init__(self, name, length, orientation, location)`: Initializes a new car object.
- `car_coordinates(self)`: Returns a list of coordinates occupied by the car on the board.
- `possible_moves(self)`: Returns a list of possible moves for the car.
- `movement_requirements(self, direction)`: Checks if a move is legal based on the car's orientation and direction.
- `move(self, move)`: Moves the car in the specified direction if possible.

### `Board` Class (board.py)

Represents the game board and manages car movements.

**Attributes:**
- `cars` (dict): A dictionary of car objects, keyed by car name.
- `size` (int): The size of the board (fixed at 7x7).

**Methods:**
- `__init__(self)`: Initializes a new game board.
- `add_car(self, car)`: Adds a car to the board if it's placement is valid.
- `move_car(self, name, movekey)`: Moves a specified car in the specified direction if the move is valid.
- `target_location(self)`: Returns the coordinate of the exit location.
- `cell_list(self)`: Returns a list of all coordinates on the board.
- `cell_content(self, coord)`: Returns the name of the car occupying the specified coordinate or None if empty.
- `__str__(self)`: Returns a string representation of the board for printing.

### `Game` Class (game.py)

Manages the game logic and user interactions.

**Attributes:**
- `board` (Board): The game board.
- `target` (str): The name of the target car (default is 'R').

**Methods:**
- `__init__(self, config_file)`: Initializes a new game using the specified JSON configuration file.
- `load_json(filename)`: Utility function to load car configurations from a JSON file.
- `play(self)`: Starts the game and manages user inputs.

### `Helper` Functions (helper.py)

**Functions:**
- `load_json(filename)`: Reads a JSON file and returns a dictionary of car configurations.

## Usage

To use this game, you need to prepare a JSON configuration file that specifies the initial positions and properties of the cars. Then, you can start the game using the following command:

```bash
python3 game.py path_to_json
