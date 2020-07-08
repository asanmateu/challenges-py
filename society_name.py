def society_name(friends):
    """ Return sorted first letter of every word in the list
    :param friends: list
    :return: string
    """
    lst = [i[0] for i in friends]
    return "".join(sorted(lst))


print(society_name(["Antonio", "Sanmateu"]))
