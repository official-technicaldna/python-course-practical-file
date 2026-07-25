try:
	x = int(input("Enter first number:"))
	y = int(input("Enter second number:"))
	print(x/y)
except Exception as error:
	print("Sorry, an error occured.")
	print(error)