import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	x = np.array(a)
	y = np.array(b)
	if len(x[0])!= len(y):
		return -1
	else:
		return np.dot(x, y)
	pass