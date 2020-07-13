
# Python got drunk and the built-in functions str() and int() are acting odd

str, int = int, str

"""Create two functions to substitute str() and int()"""

def int_to_str(num):
    return str(num)

def str_to_int(num):
    return int(num)

