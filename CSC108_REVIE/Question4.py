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
    #ur function here

if __name__ == '__main__':
    import doctest
    doctest.testmod()

