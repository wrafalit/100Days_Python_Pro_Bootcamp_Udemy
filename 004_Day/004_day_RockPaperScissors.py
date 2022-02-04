import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you coose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

game_image = [rock, paper, scissors]
print(game_image[user_choice])


computer_choice = random.randint(0,2)
print("Computer choose:\n",game_image[computer_choice])


if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
