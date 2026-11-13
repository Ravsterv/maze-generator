from tile import Tile

class Grid:

    def __init__(self):
        self._grid = []

    def set_grid(self):
        self._grid = []

    def add_row(self, row):
        self._grid.append(row)

    def get_tile(self, x, y):
        return self._grid[y][x]

    def get_adjacent(self, tile: Tile, current_maze_size: int) -> list[Tile]:
        tile_delta = [[0, 1],
                      [1, 0],
                      [0, -1],
                      [-1, 0]]
        chosen_tiles = []



        return chosen_tiles
