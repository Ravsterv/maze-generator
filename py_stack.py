# This will contain the Stack class


class Stack:
    """
    Characteristic of a Stack
        - Can only be accessed from the top
        - First In, Last Out structure.

    """

    def __init__(self):
        """


        """
        self._stack = []

    def pop(self):
        """
        take the top item off the stack

        :return:
        """
        if len(self._stack) < 1:
            assert IndexError
        tile = self._stack[-1]
        self._stack = self._stack[:(len(self._stack) - 1)]
        return tile

    def push(self, tile):
        """
        Add an item to the stack
        :return:
        """
        self._stack.append(tile)


    def peek(self):
        """
        Look at top item without removing it
        :return:
        """
        return self._stack[-1]