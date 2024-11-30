from coding_exercise.domain.model.cable import Cable


class Splitter:

    # Define methods within a class that don't require an instance of the class to be called
    @staticmethod

    # A single leading underscore is often used to indicate that a variable or method is intended
    # for internal use within a class, but not strictly enforced.
    # __ is not exclusively used for system-defined keywords.
    # While it's commonly used in specific contexts,
    # its primary purpose is to indicate special methods or attributes within a class.
    def _validate(cable: Cable, times: int):
        # Check length constraints
        if not (2 <= cable.length <= 1024):
            raise ValueError("Cable length must be between 2 and 1024.")

        # Check times constraints
        if not (1 <= times <= 64):
            raise ValueError("Times must be between 1 and 64.")

        # Ensure resulting lengths are at least 1
        if cable.length // (times + 1) < 1:
            raise ValueError("Cannot split cable into lengths less than 1.")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        # Validate the inputs
        self._validate(cable, times)

        # Calculate the base split length and remainder
        base_length = cable.length // (times + 1)
        remainder = cable.length % (times + 1)

        # Create the split cables
        result = [
            Cable(base_length, f"{cable.name}-{str(i).zfill(2)}") for i in range(times + 1)
        ]

        # Add the remainder as a single part (if any)
        if remainder > 0:
            result.append(Cable(remainder, f"{cable.name}-{str(len(result)).zfill(2)}"))

        return result

# Test easier in IDE.
if __name__ == "__main__":
    _result = Splitter().split(Cable(1000, "test"), 2)
    print([str(c) for c in _result])
