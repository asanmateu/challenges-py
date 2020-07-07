def halve_count(a,b):
    """Given two integers a and b, return how many times a can be halved while still being greater than b"""
    i = 0
    while a > b:
        a = a/2
        i += 1
    return i-1
