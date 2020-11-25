def find_bob(names):
    """ Locate Bob if he is in the list otherwise -1
    :param names: list of strings
    :return: index integer
    """
    return names.index('Bob') if 'Bob' in names else -1


print(find_bob(["Jimmy", "Layla", "Mandy"]))
print(find_bob(["Bob", "Nathan", "Hayden"]))
