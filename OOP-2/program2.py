class UserInfo():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.__password = "abcd123"
	def greet(self):
		print("Hi dear",self.name)

myUser = UserInfo("Laxman",21)
myUser.greet()
print(myUser.age)
print(myUser.__password)