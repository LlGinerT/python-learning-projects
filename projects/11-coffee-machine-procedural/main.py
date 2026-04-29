from data import MENU
from data import resources as rs


def check_resources(coffee):
    """Check if have enough resources at the machine for the selected drink."""
    coffee_ingredients = coffee["ingredients"]
    for key in coffee_ingredients:
        if coffee_ingredients[key] >= rs[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    while True:
        try:
            total = int(input("How many pennies: ")) * 0.01
            print(f"Credit: ${total:.2f}")
            total += int(input("How many nickles: ")) * 0.05
            print(f"Credit: ${total:.2f}")
            total += int(input("How many dimes: ")) * 0.10
            print(f"Credit: ${total:.2f}")
            total += int(input("How many quarters: ")) * 0.25
            print(f"Credit: ${total:.2f}")
            break
        except ValueError:
            print("Invalid input. Insert valid amount of coins")
    return total


def check_transaction(coffee, drink_name):
    """Check if the money inserted is enough for the selected drink,
    and give change."""
    cost = coffee["cost"]
    print(f"{drink_name.title()} cost: {cost:.2f}")
    print("Please insert coins.")
    inserted_money = process_coins()
    if inserted_money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money > cost:
        change = inserted_money - cost
        print(f"Here is ${change:.2f} in change.")
    rs["money"] += cost
    return True


def make_coffee(coffee, drink_name):
    if check_resources(coffee):
        if check_transaction(coffee, drink_name):
            print(f"Here is your {drink_name.title()} ☕. Enjoy!")
            for key in coffee["ingredients"]:
                rs[key] -= coffee["ingredients"][key]


def main():
    rs["money"] = 0
    while True:
        prompt = input(
            "What would you like?\n1)Espresso\n2)Latte\n3)Cappuccino\nChoice product: "
        )
        match prompt.lower():
            case "off":
                break
            case "report":
                for key in rs:
                    print(f"{key}: {rs[key]}")
            case "1":
                make_coffee(MENU["espresso"], "espresso")
            case "2":
                make_coffee(MENU["latte"], "latte")
            case "3":
                make_coffee(MENU["cappuccino"], "cappuccino")
            case _:
                print("Invalid input. Please try again.")


main()
