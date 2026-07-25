import csv
file = open("user_data.csv", "r")
data = csv.reader(file)
next(data)
for row in data:
	print(row)
file.close()