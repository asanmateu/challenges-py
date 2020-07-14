def list_of_multiples (num, length):
    """Create a function that takes two numbers as arguments (num, length)
    and returns a list of multiples of num up to length.

    :param num: int
    :param length: int
    :return:
    """

    return [num * i for i in range(1, length+1)]

print(list_of_multiples(6,7))