import random


cards = [11, 2, 3, 4, 5, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choices(cards,k=2)

user_card = deal_card()
comp_card = deal_card()

user_card_value = sum(user_card)
comp_card_value = sum(comp_card)
print(user_card,user_card_value )
print(comp_card,comp_card_value)

if user_card_value == 21:
    print("User WIN")
elif comp_card_value == 21:
    print("Comp WIN")

if user_card_value > 21:
    if not 11 in user_card:
        print("User Lose")
    else:
        if sum(comp_card) -10 > 21:
            print("User Lose")
move = input("Do you want to get another card? y/n")
if move == 'y':
    user_card.append(random.choice(cards))
    continue
else:
    while comp_card_value < 17:
        comp_card.append(random.choice(cards))
        comp_card_value = sum(comp_card)
    else:
        comp_card_value == 21:
            print("Comp WIN")

if comp_card_value > user_card_value:
    print("Comp WIN")
elif comp_card_value < user_card_value:
    print("User WIN")
else:
    print("DRAW")
        
    
