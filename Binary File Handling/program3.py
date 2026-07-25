import pickle
user_info = [
input("Enter name:"),
int(input("Enter age:")),
input("Enter gender: (male/female").lower()
]
file = open("data.dat","ab")
pickle.dump(user_info,file)
file.close()