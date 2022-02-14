MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print("Water:", resources['water'] ,"ml")   
    print("Milk:", resources['milk'] ,"ml")  
    print("Coffee:", resources['water'] ,"g")
    print("Money: $",profit)


def check_resour(order_avail):
    for item in order_avail:
        if order_avail[item] > resources[item]:
            print('Sorry there is not enough ', item)
        else:
            return True
    

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes ?: ")) * 0.1
    total += int(input("how many nickles  ?: ")) * 0.05
    total += int(input("how many pennies  ?: ")) * 0.01
    return total
    

def check_transaction(money, drink_cost):
    if money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if money > drink_cost:
            change = money - drink_cost
            print(f"Here is ${change} dollars in change")
        global profit
        profit += drink_cost
        return True
    

def make_coffee(deducted):
    # global resources
    for item in deducted:
        print(resources[item] , " - ", deducted[item])
        resources[item] -= deducted[item]
    print("Here is your latte. Enjoy!")
    # return resources


machine_on = True

while machine_on:
    user_input = input("What would you like? espresso/latte/cappuccino): ")
    if user_input == 'off':
        machine_on = False
    elif user_input == 'report':
        report()
    else:
        drink = MENU[user_input]
        if check_resour(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment,drink['cost']):
                make_coffee(drink["ingredients"])
                print(resources)
    
            
    
