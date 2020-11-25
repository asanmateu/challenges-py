import math


def century_from_year(year):
    """ Return century from year
    :param year: int
    :return: int
    """
    return math.ceil(year / 100)


print(century_from_year(1982))
print(century_from_year(2001))
