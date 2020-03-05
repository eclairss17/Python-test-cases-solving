#Get Some of squares of a digit in python
def get_digits_sum(n):
	return sum(int(c) ** 2 for c in str(n)) 