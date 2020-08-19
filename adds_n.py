def adds_n(n):
    """ Write a function that returns a lambda expression, which adds n to its input.
    :param n: int
    :return: int
    """

    return lambda x: x + n


adds1 = adds_n(1)

print(adds1(2))
print(adds1(5.7))
