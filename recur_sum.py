def recur_sum(n):
	"""Sum of the first n natural numbers"""
	if n < 1:
		return n
	else:
		return n + recur_sum(n-1)

print(recur_sum(10))
