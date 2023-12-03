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
    name_lst = []
    for i in range(0,len(contacts),2):
        name_lst.append(contacts[i])
    name_lst.sort()
    contacts_copy = contacts[:]
    contacts.clear()
    for name in name_lst:
        contacts.append(name)
        index = contacts_copy.index(name)
        contacts.append(contacts_copy[index])


if __name__ == '__main__':
    import doctest
    doctest.testmod()