class MySum():
	def do_operation(self, num1, num2):
		print("Result:",num1+num2)

class MyMultiplication():
	def do_operation(self, num1, num2):
		print("Result:",num1*num2)

class MyDivision():
	def do_operation(self, num1, num2):
		print("Result:",num2/num1)

do_sum = MySum()
do_multiply = MyMultiplication()
do_division = MyDivision()

do_sum.do_operation(1,2)
do_multiply.do_operation(3,5)
do_division.do_operation(1,2)
