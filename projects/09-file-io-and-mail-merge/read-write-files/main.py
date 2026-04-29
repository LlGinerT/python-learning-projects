from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "file.txt"

file = open(FILE_PATH)
content = file.read()
print(content)
file.close()  # Need to be closed for don't waste resources, or modify
# until the garbage colector close it

# we can use 'with' for do it more effective without remember the close method

with open(FILE_PATH) as file:
    content = file.read()
    print(content)

with open(FILE_PATH, mode="w") as file:
    # mode='w' replace all the text for the new
    # in 'w' mode if the file don't exist, create a new one
    content = file.write("New text.")

with open(FILE_PATH, mode="a") as file:
    # mode='a' append the text
    content = file.write("\nNew text.")
