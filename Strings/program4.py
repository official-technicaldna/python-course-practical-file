msg = input("Enter your message:")
name = input("Enter your name:")
msg_text = """
Hello [name]!
"""+msg
msg_text = msg_text.replace("[name]",name)
print(msg_text)
