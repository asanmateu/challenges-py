def cars(wheels, bodies, figures):
    """Return number of complete toy cars that can be made"""
    return min(wheels // 4, bodies, figures // 2)


print(cars(6, 3, 25))
