def next_in_line(lst, num):
    """Write a function that takes a list and a number as arguments.
        Add the number to the end of the list, then remove the first
        element of the list. The function should then return the updated list.

    :param lst: list
    :param num: int
    :return: list
    """
    if len(lst) != 0:
        lst.pop(0)
        lst.append(num)
        return lst
    else:
        return "No list has been selected"
