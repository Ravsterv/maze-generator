from tile import Tile
from variables import *


class Grid:

    def __init__(self):
        self._grid = []

    def set_grid(self):
        self._grid = []



    def get_grid_size(self):
        return len(self._grid)

    def add_row(self, row: list[Tile]):
        self._grid.append(row)

    def get_tile(self, x, y) -> Tile | None:
        if x < 0 or y < 0:
            return None
        if x >= len(self._grid[0]) or y >= len(self._grid):
            return None
        return self._grid[y][x]

    def get_adjacent(self, tile: Tile, current_maze_size: int, phase: int) -> list[Tile]:
        """

        :param tile: Current tile
        :param current_maze_size: Maze size required for
        :param phase: 1 ,2 if in phase 2, it won't consider Maze path restrictions
        :return:
        """
        tile_delta = [[0, 1],
                      [1, 0],
                      [0, -1],
                      [-1, 0]]
        chosen_tiles = []
        x, y = tile.get_cord()
        # In this find adjacent tiles
        for delta in tile_delta:

            adj_tile = self.get_tile(x + delta[0], y + delta[1])

            if adj_tile is None:
                continue

            # if phase is 1 and you exceed the minimum maze size, you can select an edge as a valid tile
            if adj_tile.is_edge_tile(self.get_grid_size()) and current_maze_size >= MINIMUM_SIZE and phase == 1:
                chosen_tiles.append(adj_tile)
                continue

            # Otherwise if it is an edge, just ignore
            if adj_tile.is_edge_tile(self.get_grid_size()) or adj_tile.get_path():
                continue

            adj_x, adj_y = adj_tile.get_cord()
            valid_tile = True

            # Check that the adjacent tiles to the adj_tile aren't open(open tiles would create a new path
            for adj_delta in tile_delta:
                tile_check = self.get_tile(adj_x + adj_delta[0], adj_y + adj_delta[1])
                if tile_check is not None:
                    if tile_check.get_path() and tile_check != tile:
                        valid_tile = False

            # Append valid tiles to list which we then check those tiles for adjacency
            if valid_tile:
                chosen_tiles.append(adj_tile)


        # Possibly create a second function to check if Adjacent tiles don't break tile rules?

        return chosen_tiles

    def display(self) -> str:
        """
        Will print the grid in a visual style of a maze

        :return:
        """
        maze_str = ""

        for row in self._grid:
            for col in row:
                if not col.get_path():
                    maze_str += (chr(9608))
                else:
                    maze_str += " "
            maze_str += "\n"
        return maze_str



