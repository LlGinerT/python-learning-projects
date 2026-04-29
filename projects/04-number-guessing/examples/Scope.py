# Modifying Global Scope

""" enemies = 1 # Global Scope

def increase_enemies():
    enemies = 2 # Local Scope
    print(f"enemies inside function: {enemies}")

increase_enemies() # print local scope
print(f"enemies outside function: {enemies}")  # print global scope  
 """

enemies = 1  # Global Scope


def increase_enemies():  # try to avoid
    global enemies
    enemies += 1  # Global now instead local
    print(f"enemies inside function: {enemies}")


increase_enemies()  # print global scope
print(f"enemies outside function: {enemies}")  # print global scope


def correct_increase_enemies(enemy):  # better practice
    return enemies + 1
