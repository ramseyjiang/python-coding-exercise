import sys


class Cable:

    def _set_length(self, length: int):
        # The requirement mentioned the maximum length is 1024, so I change the sys.maxsize to 1024.
        if not isinstance(length, int) or length < 0 or length > 1024:
            raise ValueError

        self.length = length

    def __init__(self, length: int, name: str):
        self._set_length(length)
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Cable):
            return self.length == other.length and self.name == other.name

        return False

    # It is used for output name and length directly during IDE test,
    def __str__(self):
        return f"{self.name}-{self.length}"