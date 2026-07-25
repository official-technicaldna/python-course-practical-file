import json
file = open("user_info.json", "w")
user_info = {
"name": input("Enter your name:"),
"age": int(input("Enter your age:"))
}
json.dump(user_info, file, indent=4)