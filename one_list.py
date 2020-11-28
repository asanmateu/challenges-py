def one_list(lst):
    """ Flatten a list of lists
    :param lst: list of lists
    :return: list
    """
    return [y for x in lst for y in x]


print(one_list([[1, 2], [3, 4]]))
