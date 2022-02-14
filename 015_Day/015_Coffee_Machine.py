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


def check_resour(order_avail):
    for item in order_avail:
        if order_avail[item] > resources[item]:
            print('Sorry there is not enough ', item)
        else:
            return True
    
    
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
            print("its ok")
    
            
    
