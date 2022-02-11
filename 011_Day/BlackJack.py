import random


cards = [11, 2, 3, 4, 5, 7, 8, 9, 10, 10, 10, 10]


def game():
    user_card = random.choices(cards,k=2)
    comp_card = random.choices(cards,k=2)
    game_off = False
    
    while not game_off:
        while True:
            user_card_value = sum(user_card)
            comp_card_value = sum(comp_card)
            print(user_card,user_card_value," User" )
            print(comp_card,comp_card_value," Comp")
            
            if user_card_value == 21:
                print("User WIN")
                break
            elif comp_card_value == 21:
                print("Comp WIN")
                break
            
            if user_card_value > 21:
                if not 11 in user_card:
                    print("User Lose")
                    break
                else:
                    if sum(comp_card) -10 > 21:
                        print("User Lose")
                        break
            move = input("Do you want to get another card? y/n ")
            if move == 'y':
                user_card.append(random.choice(cards))
                continue
            else:
                while comp_card_value < 17:
                    comp_card.append(random.choice(cards))
                    comp_card_value = sum(comp_card)
                    print(user_card,user_card_value," User" )
                    print(comp_card,comp_card_value," Comp")
                else:
                    if comp_card_value == 21:
                        print("Comp WIN 45")
                        break
            
            if comp_card_value > user_card_value:
                print("Comp WIN 48")
            elif comp_card_value < user_card_value:
                print("User WIN")
            else:
                print("DRAW")
                
            
        if input("Do you want game again? y/n ") == 'n':
            game_off = True
        else:
            game()

game()
        
    
