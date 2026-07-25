import random
names = ["Laxman", "Technical DNA", "Shubham","Shubhankar"]
chosen_name = random.choice(names)
print("Hello",chosen_name,"! Your name has been selected.")
chosen_names = random.choices(names, k=3, weights=[1,2,1,1])
print(chosen_names)
non_repeted_names = random.sample(names, k=3)
print(non_repeted_names)