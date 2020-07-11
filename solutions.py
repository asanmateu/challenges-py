def solutions(a, b, c):
    """A quadratic equation a x² + b x + c = 0 has either
        0, 1, or 2 distinct solutions for real values of x.
        Given a, b and c, you should return the number of
        solutions to the equation."""
    i = (b ** 2) - 4 * a * c
    if i == 0:
        return 1
    elif i > 0:
        return 2
    else:
        return 0
