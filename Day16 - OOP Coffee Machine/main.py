from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
response = ""

while response != "off":
    response = input(f"What would you like? ({menu.get_items()}): ")
    if response == "report":
        coffee_maker.report()
        money_machine.report()
    elif response != "off":
        order = menu.find_drink(response)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
