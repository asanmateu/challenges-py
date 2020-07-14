def digit_count(n):
    ''' For every digit in the number, replace that digit
        with how many times it appears in the number.
    :param n: integer
    :return: integer
    '''
    lst = [int(i) for i in str(n)]
    return int("".join(str(lst.count(d)) for d in lst))