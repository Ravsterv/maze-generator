class Tile:
    def __init__(self, x, y):
        self._on_path = False
        self._x = x
        self._y = y
        self._previously_backed = False

    def get_path(self):
        return self._on_path

    def set_path(self):
        self._on_path = not self._on_path

    def set_back_track(self):
        self._previously_backed = not self._previously_backed

    def get_back_track(self):
        return self._previously_backed

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

        if self._x == grid_size-1 or self._y == grid_size-1:
            is_edge = True

        return is_edge

    def __eq__(self, other):

        return other.get_cord() == self.get_cord()

    def __str__(self):
        return f"Tile({self._x},{self._y})"
