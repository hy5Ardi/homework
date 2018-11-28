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

def getIndex(array, i):
	index = 0
	for e in array:
		if e == i:
			return index
		else:
			index += 1

index = getIndex(numbers, 75)
print(index)