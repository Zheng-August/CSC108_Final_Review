def swap_rows_and_columns(grid: list[list[int]]) -> None:
    """Modify grid so that each row in grid is swapped with the corresponding column.
    For example, row 0 is swapped with column 0, row 1 is swapped with column 1, and so on.
    Precondition: each list in grid has the same length as grid and len(grid) >= 2
    >>> G2 = [[1, 2],
    ...       [3, 4]]
    >>> swap_rows_and_columns(G2)
    >>> G2 == [[1, 3],
    ...        [2, 4]]
    True
    >>> G3 = [[1, 2, 3],
    ...       [4, 5, 6],
    ...       [7, 8, 9]]
    >>> swap_rows_and_columns(G3)
    >>> G3 == [[1, 4, 7],  
    ...        [2, 5, 8],
    ...        [3, 6, 9]]
    True
    """
    n = len(grid)  # Assuming it's a square matrix as per the precondition
    for i in range(n):
        for j in range(i + 1, n):  # Start from i + 1 to avoid swapping elements on the diagonal
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

