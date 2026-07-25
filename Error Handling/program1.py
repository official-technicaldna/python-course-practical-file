try:
	x = int(input("Enter first number:"))
	y = int(input("Enter second number:"))
	print(x/y)

except ZeroDivisionError:
	print("Sorry, you can't divide any number by 0.")

except ValueError:
	print("Error, only numarical values are allowed.")

except:
	print("Sorry, an unknown error occured...")

finally:
	print("Program finished!")