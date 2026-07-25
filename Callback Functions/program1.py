def takeNumbers(sum_nums):
	a = int(input("enter first number:"))
	b = int(input("Enter second number:"))
	return sum_nums(a,b)

def mySum(num1,num2):
	return num1+num2
x = takeNumbers(mySum)
print("The sum of numbers is:",x)