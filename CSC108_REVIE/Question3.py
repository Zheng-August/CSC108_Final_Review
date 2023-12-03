'''
Complete this function according to its docstring by implementing the algorithm below:
    1. Use an integer accumulator to keep track of the number of matches.
    2. For each item in lst, compare it to all other items in lst and if the item matches an item other than itself, add to
    the number of matches.
    3. Return the number of duplicates.
Note: you must not use any list methods, but you may use the built-in function len().
To earn marks for this question, you must follow the algorithm described above.

'''

def count_duplicates_v1(lst: list[int]) -> int:
    """Return the number of duplicates in lst.
    Precondition: each item in lst occurs either once or twice.
    >>> count_duplicates_v1([1, 2, 3, 4])
    0
    >>> count_duplicates_v1([2, 4, 3, 3, 1, 4])
    2
    """
    # Your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
