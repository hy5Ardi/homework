operation = input("What you would like to calculate?: ")
splitted = operation.split(" ")

if len(splitted) != 3:
	print("Error: You have to insert correct calculation. Example: 3 + 3")

first, type, second = splitted

first = int(first)
second = int(second)

if type == "+":
	summation = first + second
	print(f"Calculation: {first} + {second} = {summation}")
elif type == "-":
	subtraction = first - second
	print(f"Calculation: {first} + {second} = {subtraction}")
elif type == "*":
	multiplication = first * second
	print(f"Calculation: {first} + {second} = {multiplication}")
elif type == "/":
	split = first / second
	print(f"Calculation: {first} + {second} = {split}")
else:
	print("Error: Invalid operation type. Please use (+; -; *; /;).")