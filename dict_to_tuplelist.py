def dict_to_list(d):
    """ Convert dictionary to list of tuples in alphabetical order
    :param d: dict
    :return: list of tuples
    """
    return sorted([(k, v) for k, v in d.items()])


d1 = {'D': 1, 'B': 2, 'C': 3}
d2 = {'likes': 2, 'dislikes': 3, 'followers': 10}

print(dict_to_list(d1))
print(dict_to_list(d2))

"""ALTERNATIVE

def dict_to_list(d):
	return sorted(d.items())
	
"""
