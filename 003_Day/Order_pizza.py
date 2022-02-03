# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

small = 15
medium = 20
large = 25

p_s = 2
p_m_l = 3
cheese = 1

if size == 's':
    bill = small
elif size == 'm':
    bill = medium
elif size == 'l':
    bill = large
else:
    print("Wrong letter")

if add_pepperoni == 'Y':
    if size == 's':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1

print("Your final bill is: $",bill)

