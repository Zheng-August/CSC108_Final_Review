def sort_contacts(contacts: list[str]) -> None:
    '''contacts contains names and phone numbers in this format:
    [name1, phone_number1, name2, phone_number2, ...]
    It's guaranteed to have an even length and that each name is unique.
    Sort the contact information so that the names are in alphabetical order.
    >>> contacts = ['Rutwa', '921', 'Dan', '777', 'Angela', '876']
    >>> sort_contacts(contacts)
    >>> contacts
    ['Angela', '876', 'Dan', '777', 'Rutwa', '921']
    '''
    # Your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
