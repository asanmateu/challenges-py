def can_alternate(s):
    """ Return True if 1s and 0s can alternate
    :param s: string 1s and 0s
    :return: boolean
    """
    return 1 >= abs(s.count('0') - s.count('1'))


print(can_alternate('1010011'))
print(can_alternate('0001100'))