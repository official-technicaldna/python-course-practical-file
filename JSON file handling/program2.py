import json
file = open("user_info.json", "r")
user_info = json.load(file)
print(user_info)