dict = {'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'}


def relation_to_luke(name):
    name = dict.get(name)
    return ("Luke, I am your {}.".format(name))


print(relation_to_luke('Darth Vader'))
