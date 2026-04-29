import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# For store the functions without trigger it, don't add the parenthesis
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(art.calculator)
    should_accumulate = True
    n1 = float(input("Type the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        n2 = float(input("Type the second number: "))
        answer = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")
        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. "
        )
        if choice.lower() == "y":
            n1 = answer
        else:
            should_accumulate = False
            end = input("Type 'y' for new calculation or 'n' to end. ")
            if end == "y":
                print("\n" * 20)
                calculator()


calculator()
