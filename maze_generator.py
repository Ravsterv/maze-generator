# Maze Generation making use of Stack and/or List data structures
import random

from py_stack import Stack
from tile import Tile
from grid import Grid

MAZE_SIZE = 10 # Min size ~ 4
MINIMUM_SIZE = 5 # force path to have a minimum length before terminating


def main():
    STARTING_SIDE = ["NORTH", "SOUTH", "EAST", "WEST"]


    maze_path = Stack()
    grid = Grid()

    # First generate map by filling grid with tiles
    for i in range(MAZE_SIZE):
        new_row = []
        for j in range(MAZE_SIZE):
            new_tile = Tile(i, j)
            new_row.append(new_tile)

        grid.add_row(new_row)



    # Now start Phase 1, generate a path that goes though the block
    #Fist, choose a location on the edge to start from
    # Select from NORTH, SOUTH, EAST, WEST then choose from 1:N-1
    chosen_direction = random.choice(STARTING_SIDE)
    random_tile = random.randint(1, MAZE_SIZE-2)

    match chosen_direction:
        case "NORTH":
            chosen_tile = grid.get_tile(random_tile, 0)
        case "SOUTH":
            chosen_tile = grid.get_tile(random_tile, MAZE_SIZE-1)
        case "EAST":
            chosen_tile = grid.get_tile(MAZE_SIZE-1, random_tile)
        case "WEST":
            chosen_tile = grid.get_tile(0, random_tile)

    maze_path.push(chosen_tile)
    # Once a side is chosen now we start iterating over the stack until
    # an edge is met + a minimum size is counted

    # Conditions for selecting a Next_Tile:
    # - Is not an edge tile(unless above min-path-size, otherwise start Phase 2)
    # - No side of the tile connects to any existing tile
    #       i.e. if that tile was chosen, it won't connect to existing lines
    # If no tile can be selected, remove top of stack and repeat.
    # If the tile meets all conditions, add to stack and repeat.
    while len(maze_path) < MINIMUM_SIZE and not maze_path.peek().is_edge_tile(MAZE_SIZE):
        possible_tiles = []




    # Phase 2: Backtrack through Stack to add distractor routes
    # Look at top tile in stack
    # see if any tiles adjacent can be added to stack following same rules as above
    # If possible, randomly push 1 valid tile to stack and repeat
    # if no spots exist, pop stack and repeat.


if __name__=="__main__":
    main()
