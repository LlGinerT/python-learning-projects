# default arguments
def default(a, b=True, c=2):
    # a = argumento obligatorio
    # b,c = default y opcional cambiarlo
    print(a, b, c)


# *args, unlimited positional arguments
def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)


add(2, 2)
add(2, 2, 2)
add(2, 2, 2, 2)


# **kwargs: Many Keyword Arguments, dictionary
def kwargsExample(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["example"])


kwargsExample(example=1, example2=2)


def calculate(n, **kwargs):
    if "add" in kwargs:
        n += kwargs["add"]
    if "multiply" in kwargs:
        n *= kwargs["multiply"]
    print(n)


calculate(2, add=2)  # 4
calculate(2, multiply=3)  # 6
calculate(2, add=2, multiply=3)  # 12


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)  # Skyline
print(my_car.colour)  # None
