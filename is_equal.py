def is_equal(lst):
    """Write function that takes a list with two numbers in it and determines if the sum of
    the digits of the two numbers are equal to each other."""

    x = list(map(lambda i: sum(int(n) for n in str(i)), lst))
    if x[0] == x[1]:
        return True
    else:
        return False


print(is_equal([42, 33]))
