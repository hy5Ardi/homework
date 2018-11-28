numbers = [
	2,
	75,
	3,
	15
]

def getMinimum(array):
	minimum = None
	for num in array:
		if not minimum or num < minimum:
			minimum = num
	return minimum

minimum = getMinimum(numbers)
print(minimum)