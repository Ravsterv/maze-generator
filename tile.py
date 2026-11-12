class Tile:
    def __init__(self):
        self._on_path = False

    def get_path(self):
        return self._on_path

    def set_path(self):
        self._on_path = True