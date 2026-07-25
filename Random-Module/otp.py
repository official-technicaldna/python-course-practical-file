import random
length = int(input("Enter the OTP length:"))
otp = ""
x = 1
while x<=length:
	otp = otp+str(random.randint(0,9))
	x += 1
print("Your OTP is:",otp)