import ingredients
from ingredients import MENU
from ingredients import resources

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def isAvailable(order):
    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif order != "espresso" and MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def report():
    print(
        f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")


def getMoney(order):
    goal = MENU[order]["cost"]
    qu = int(input("How many quarters?: "))
    di = int(input("How many dimes?: "))
    ni = int(input("How many nickels?: "))
    pe = int(input("How many pennies?: "))
    inserted = qu * quarters + di * dimes + ni * nickles + pe * pennies

    if inserted >= goal:
        print("Here is your change: $" + str(inserted - goal))
        make(order)
        print(f"Here is your {order}. Enjoy!")
        ingredients.resources["money"] += goal
    else:
        print("Sorry that's not enough money. Money refunded.")
        inserted = 0


def make(order):
    if order != "espresso":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    resources["water"] -= MENU[order]["ingredients"]["water"]


selection = ""
canDo = True
while selection != "off":
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "report":
        report()
    elif selection != "off":
        canDo = isAvailable(selection)
        if canDo:
            getMoney(selection)
