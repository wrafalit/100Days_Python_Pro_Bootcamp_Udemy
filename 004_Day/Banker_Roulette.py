# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_name = len(names) - 1
los = random.randint(0,len_name)
print(names[los]," is going to buy meal today")

print(random.choice(names)," is going to buy meal today")