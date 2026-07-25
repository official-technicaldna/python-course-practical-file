import csv
with open("students_marks.csv", "w", newline="") as file:
	data = [
	["Name","Marks"],
	["Laxman", 95],
	["Amit", 30],
	["Abhishekh", 85]
	]
	writer = csv.writer(file)
	writer.writerows(data)
