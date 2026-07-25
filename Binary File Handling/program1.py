import pickle
file = open("data.dat", "wb")
data = ["Laxman","Sumit","Shubham","Sunita"]
pickle.dump(data,file)
file.close()