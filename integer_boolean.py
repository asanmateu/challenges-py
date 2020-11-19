def integer_boolean(n):
    """True for 1"""
    return [int(i) == 1 for i in n]

print(integer_boolean("100101"))
print(integer_boolean("101101011010101"))