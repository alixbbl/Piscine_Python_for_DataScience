import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a list in 2D, converts it in an array using the numpy lib,
    then, if the arguments are correct, slices it using the semi-colon syntax:
    [start:end].
    """
    family_array = np.array(family)
    rows, cols = family_array.shape
    if start < 0 or start >= rows:
        raise ValueError("Start index out of bounds")
    if end > rows:
        raise ValueError("End index out of bounds")

    sliced_array = family_array[start:end]
    new_rows, new_cols = sliced_array.shape
    print("My shape is : (", rows, ",", cols, ")")
    print("My new shape is : (", new_rows, ",", new_cols, ")")
    return sliced_array.tolist()
