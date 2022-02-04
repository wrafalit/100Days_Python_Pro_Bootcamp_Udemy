import random

ran_h_t = random.randint(0,1)
print(ran_h_t)
h_t = input("Heads or Tails?\n")



if h_t == 'Heads' and  ran_h_t == 1:
    print("You win!")
elif h_t == 'Tails' and  ran_h_t == 0:
    print("You win!")
else:
    print("You Lose!")