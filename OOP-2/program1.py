class MyMath():
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def doSum(self):
		print("Result:",self.num1+self.num2)

math_operation = MyMath(3,5)
math_operation.doSum()