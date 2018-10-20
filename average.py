array = []

for i in range(1, 4):
	numbers = int(input(f"Enter number {i}: "))
	array.append(numbers)

average = sum(array) / 3

print()
print(f"The average of numbers is {average}")