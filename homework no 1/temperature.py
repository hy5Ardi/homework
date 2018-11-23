def convert_celsius_to_fahrenheit(celsius):
	fahrenheit = (celsius *  9 / 5) + 32
	print(f"{celsius}°C is equal to {fahrenheit}°F")

def conver_fahrenheit_to_celsius(fahrenheit):
	celsius = (fahrenheit - 32) * 5 / 9
	print(f"{fahrenheit}°F is equal to {celsius}°C")

print()
print(" 1. Celsius -> Fahrenheit")
print(" 2. Fahrenheit -> Celsius")
print()
selection = input("Please select operation. (1/2) ")

if selection == "1":
	celsius = int(input("Insert temeprature in Celsius: "))
	convert_celsius_to_fahrenheit(celsius)
elif selection == "2":
	fahrenheit = int(input("Insert temeprature in Fahrenheit: "))
	conver_fahrenheit_to_celsius(fahrenheit)
else:
	print("Error: Invalid input.")