def print_stars(rows, cols):
    """
    Print a grid of stars with the given number of rows and columns.

    Parameters:
    rows (int): Number of rows in the grid.
    cols (int): Number of columns in the grid.
    """
    for _ in range(rows):
        print("* " * cols)


# Let's use this function to print a grid of stars with 6 rows and 11 columns
print_stars(7, 12)
