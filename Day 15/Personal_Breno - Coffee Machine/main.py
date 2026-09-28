from random import choice

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

#TODO 3. Verify if there are enough resources to make that drink
def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

#TODO 4. Process coins
def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please, insert coins\n")
    total = 0
    total += int(input("How many quarters ($0.25) ?"))*0.25
    total += int(input("How many dimes ($0.1) ?"))*0.1
    total += int(input("How many nickles ($0.05) ?"))*0.05
    total += int(input("How many pennies ($0.01) ?"))*0.01
    return total

#TODO 5. Check transaction
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"\nSorry, you don't have enough. The drink cost ${drink_cost}. Your money is ${money_received}. Money refunded.")
        return False

#TODO 6. Make Coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


#TODO 2. The machine should be turned off for maintenance.
is_the_machine_on = True

#TODO 1. The prompt should show again to serve the next customer
while is_the_machine_on:
    choice = input("\nWhat would you like? (espresso, latte, cappuccino)\n")
    if choice == "off":
        is_the_machine_on = False
    # Print "report" should generate a report that contains the current resource values.
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(f"Your drink cost: ${drink["cost"]}\n")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
