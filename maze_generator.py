# Maze Generation making use of Stack and/or List data structures
import random

from py_stack import Stack
from tile import Tile
from grid import Grid
import time
import os
from variables import *



def main():
    previously_stuck = False
    stuck_back_track = 0
    STARTING_SIDE = ["NORTH", "SOUTH", "EAST", "WEST"]
    maze_path = Stack()
    grid = Grid()

    # First generate map by filling grid with tiles
    for i in range(MAZE_SIZE):
        new_row = []
        for j in range(MAZE_SIZE):
            new_tile = Tile(j, i)
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

    chosen_tile.set_path()
    maze_path.push(chosen_tile)
    # Once a side is chosen now we start iterating over the stack until
    # an edge is met + a minimum size is counted

    # Conditions for selecting a Next_Tile:
    # - Is not an edge tile(unless above min-path-size, otherwise start Phase 2)
    # - No side of the tile connects to any existing tile
    #       i.e. if that tile was chosen, it won't connect to existing lines
    # If no tile can be selected, remove top of stack and repeat.
    # If the tile meets all conditions, add to stack and repeat.
    while len(maze_path) < MINIMUM_SIZE or not maze_path.peek().is_edge_tile(MAZE_SIZE):

        time.sleep(0.2)
        os.system("cls")
        print(f"Current Tile: {maze_path.peek()}")

        possible_tiles = grid.get_adjacent(maze_path.peek(), len(maze_path), 1)
        print(possible_tiles)
        print(grid.display())
        # if no tile fits conditions, pop top tile

        # improve back track to mark tiles previously back tracked too to further back tracking
        if len(possible_tiles) == 0:
            # swap tile to no longer path

            reset_tile = maze_path.pop()
            reset_tile.set_path()
            while True:
                if maze_path.peek().get_back_track():
                    maze_path.pop().set_path()
                else:
                    break

            maze_path.peek().set_back_track()
            continue



        new_tile = random.choice(possible_tiles)
        new_tile.set_path()
        maze_path.push(new_tile)




        #print("\n\n\n")

    # Phase 2: Backtrack through Stack to add distractor routes
    # Look at top tile in stack
    # see if any tiles adjacent can be added to stack following same rules as above
    # If possible, randomly push 1 valid tile to stack and repeat
    # if no spots exist, pop stack and repeat.
    # Use two stacks, when adding new tiles and after looking at a tile pop and push it to the new stack
    # don't transfer if no possible locations exist

    phase2_stack = Stack()
    os.system("cls")
    print(grid.display())

    while len(maze_path) != 0 or len(phase2_stack) != 0:
        if len(maze_path) == 0:
            # Reset the stack once all have swapped over, note this reverses stack order
            maze_path = phase2_stack
            phase2_stack = Stack()
        # Find possible locations the tile can go looking at the top
        new_tiles = grid.get_adjacent(maze_path.peek(), MAZE_SIZE, 2)
        if len(new_tiles) == 0:
            maze_path.pop()
            continue

        # Choose tile, add to secondary stack
        b_tile = random.choice(new_tiles)
        b_tile.set_path()
        phase2_stack.push(b_tile)
        phase2_stack.push(maze_path.pop())

        os.system("cls")
        print(grid.display())
        time.sleep(0.05)


if __name__ == "__main__":
    main()
