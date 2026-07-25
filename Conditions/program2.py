print("""
1. First option
2. Second option
3. Third option
""")
option = int(input("Enter option number to select:"))
match option:
	case 1:
		print("First option is selected!")
	case 2:
		print("Second option is selected!")
	case 3:
		print("Third option is selected!")
	case _:
		print("Sorry, invalid option number specifyed...")