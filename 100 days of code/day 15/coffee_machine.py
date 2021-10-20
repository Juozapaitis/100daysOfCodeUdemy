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

# print report
def check_if_enough_money(quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted, choice):
    coffee_price = MENU[choice]["cost"]
    coin_price = quarters_inserted * 0.25 + dimes_inserted * 0.1 + nickels_inserted * 0.05 + pennies_inserted * 0.01
    enough_resources = True
    global profit

    if coin_price < coffee_price:
        return False
    elif coin_price == coffee_price:
        profit += coffee_price
        print(f"Here is your {choice}")
        return True
    else:
        profit += coffee_price
        print(f"Here is your {choice}. And here is your ${coin_price - coffee_price:.2f} in change")
        return True

def check_if_enough_resources(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True
        

def report(choice):
    money_left = profit
    print(f"Water: {resources['water']}ml ")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g ")

    if money_left != 0:
        print(f"Money: ${money_left} ")

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    # print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        report(choice)
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        if check_if_enough_resources(choice):
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickels_inserted = int(input("How many nickels?: "))
            pennies_inserted = int(input("How many pennies?: "))
            if check_if_enough_money(quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted, choice):
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded")

