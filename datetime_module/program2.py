from datetime import date
course_registration_date = date.today()
course_validity_date = date(course_registration_date.year,course_registration_date.month+1,course_registration_date.day)
#print("your course is valid till:",course_validity_date)
if course_registration_date.year <= course_validity_date.year and course_registration_date.month <= course_validity_date.month and course_registration_date.day <= course_validity_date.day:
	print("The course is valid!")
else:
	print("Sorry, the course has expired.")