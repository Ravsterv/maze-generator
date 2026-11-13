class Tile:
    def __init__(self, x, y):
        self._on_path = False
        self._x = x
        self._y = y

    def get_path(self):
        return self._on_path

    def set_path(self):
        self._on_path = True

    def get_cord(self):
        return self._x, self._y

    def is_edge_tile(self, grid_size):
        """
        Checks if tile is considered an edge tile.
        :param grid_size:
        :return:
        """
        is_edge = False

        if self._x == 0 or self._y == 0:
            is_edge = True

        if self._x == grid_size or self._y == grid_size:
            is_edge = True

        return is_edge

    def __eq__(self, other):

        return other.get_cord() == self.get_cord()
