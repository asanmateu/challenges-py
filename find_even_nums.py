def find_even_nums(num):
    """ Return all even numbers above 0 up to num
    :param num: int
    :return: list of ints
    """
    return [i for i in range(1, num+1) if i % 2 == 0]

print(find_even_nums(10))