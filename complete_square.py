def complete_square(lst):
	"""Write a function that pads a rectangular matrix with zeros
	 on the right or at the bottom to make it square."""

	if len(lst[0]) > len(lst):
		while len(lst[0]) > len(lst):
			lst += [[0 for i in range(len(lst[0]))]]
		return lst
	else:
		while len(lst) > len(lst[0]):
			for i in lst:
				i.append(0)
	return lst

print(complete_square([[1,2],
					   [3,5],
					   [4,5]]))
