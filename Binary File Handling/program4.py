import pickle
data = []
file = open("data.dat","rb")
while True:
	try:
		data.append(pickle.load(file))
	except EOFError:
		break
file.close()
print(data)