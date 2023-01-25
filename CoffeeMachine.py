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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def store_cash(cost):

    global cash_stored
    cash_stored += cost
    return cash_stored




def take_cash(cash, drink,water,milk,coffee,cost):
    print(f"That'll be €{cost} euros")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickelss?: ")
    pennies = input("How many pennies?: ")


    cash = 0.25 * float(quarters) + 0.1 * float(dimes) + 0.05 * float(nickels) + 0.01 * float(pennies)


    change = cash - cost
    if change < 0:
        print("Insufficient funds, money refunded")
    else:
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee

        return print(f"Thank you, please take your change of €{round(change, 2)} and enjoy your {drink}"), store_cash(cost), resources["water"], resources["milk"], resources["coffee"]





def makecappuccino():
    if (resources["water"] >= 250) and (resources["milk"] >= 100) and (resources["coffee"] >= 24):
        take_cash(cash, "cappuccino",250,100,24,3.0)
    else:
        print("Coffee machine must be refilled")

def make_espresso():
    if (resources["water"] >= 50) and (resources["milk"] >= 0) and (resources["coffee"] >= 18):
        take_cash(cash, "espresso",50,0,18,1.50)
    else:
        print("Coffee machine must be refilled")

def make_latte():
    if (resources["water"] >= 200) and (resources["milk"] >= 150) and (resources["coffee"] >= 24):
        take_cash(cash, "latte",200,150,24,2.50)
    else:
        print("Coffee machine must be refilled")




cash = 0
change = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
cash_stored = 0

order_coffee = True
while order_coffee == True:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "cappuccino":
        makecappuccino()
    elif choice == "espresso":
        make_espresso()
    elif choice == "latte":
        make_latte()
    elif choice == "report":
        print(f"Water = {resources['water']}ml\n")
        print(f"Milk = {resources['milk']}ml\n")
        print(f"Coffee = {resources['coffee']}g\n")
        print(f"Money = €{cash_stored} euros\n")
    elif choice == "refill":
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print("Thanks for refilling. \n")
    elif choice == "off":
        exit()





