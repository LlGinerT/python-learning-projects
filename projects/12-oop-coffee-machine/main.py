from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money = MoneyMachine()
    while True:
        prompt = input(f"What would you like? {menu.get_items()}\nChoice product: ")
        if prompt == "off":
            break
        elif prompt == "report":
            coffee_maker.report()
            money.report()
        else:
            order = menu.find_drink(prompt)
            if order == None:
                continue
            elif coffee_maker.is_resource_sufficient(order) and money.make_payment(
                order.cost
            ):
                coffee_maker.make_coffee(order)


main()
