# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1 + name2).lower()
t_o = name.count('t')
r_o = name.count('r')
u_o = name.count('u')
e_o = name.count('e')
true_sum = t_o + r_o + u_o + e_o

l_o = name.count('l')
o_o = name.count('o')
v_o = name.count('v')
ee_o = name.count('e')
love_sum = l_o + o_o + v_o + ee_o

love_score = str(true_sum) + str(love_sum)
print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < int(love_score) < 50:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
else:
    print("Your score is ", love_score)