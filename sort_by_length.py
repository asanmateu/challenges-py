def sort_by_length(lst):
    """ Return a list of strings sorted by length of elements
    :param lst: list of strings
    :return: list of strings
    """
    return sorted(lst, key=len)


print(sort_by_length(["len", "length", "tiburon", "pl"]))