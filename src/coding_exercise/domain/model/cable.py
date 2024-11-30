import sys


class Cable:

    def _set_length(self, length: int):
        if not isinstance(length, int) or length < 0 or length > sys.maxsize:
            raise ValueError

        self.length = length

    def __init__(self, length: int, name: str):
        self._set_length(length)
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Cable):
            return self.length == other.length and self.name == other.name

        return False
