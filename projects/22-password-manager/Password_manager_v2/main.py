import json
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_elements = [choice(letters) for num in range(randint(6, 8))]
    password_elements += [choice(symbols) for num in range(randint(2, 4))]
    password_elements += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_elements)

    password = "".join(password_elements)

    password = password[:10]

    if not any(symbol in password for symbol in symbols) or not any(
        num in password for num in numbers
    ):
        password_generator()
    else:
        password_input.delete(0, END)
        password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_input.get()

    # Dictionary for test if a field are empty
    fields = {"Website": website, "Email": email, "Password": password}
    empty_fields = [field for field in fields if len(fields[field]) == 0]

    # Dictionary for store new data
    new_data = {
        website.lower(): {
            "email": email,
            "password": password,
        }
    }

    if len(empty_fields) == 0:
        try:
            with open(DATA_PATH, mode="r") as data_file:
                # Reading existing data
                data = json.load(data_file)
                # Updating the data
                data.update(new_data)
                data_to_store = data
        except FileNotFoundError:
            data_to_store = new_data
        finally:
            with open(DATA_PATH, mode="w") as data_file:
                json.dump(data_to_store, data_file, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "test@test.com")
        password_input.delete(0, END)
        website_entry.focus()

    else:
        message_field = ""
        for field in empty_fields:
            if len(message_field) == 0:
                message_field += f"Ooops!\n{field}"
            else:
                message_field += f", {field}"
        if len(empty_fields) > 1:
            message_field += " fields are empty."
        else:
            message_field += " field is empty."
        message_field += "\nPlease entry all required fields."
        messagebox.showerror(title="Empty field", message=f"{message_field}")


# ---------------------------- Show data ------------------------------- #
def find_data():
    website = website_entry.get().lower()
    try:
        with open(DATA_PATH, mode="r") as data_file:
            data = json.load(data_file)
        email = data[website]["email"]
        password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data stored")
    except KeyError:
        messagebox.showerror(
            title="Invalid Website", message=f"No details for {website} exists."
        )
    else:
        messagebox.showinfo(
            title=f"{website.title()}", message=f"Email: {email}\nPassword: {password}"
        )


# ---------------------------- UI SETUP ------------------------------- #
sc = Tk()
sc.title("Password Manager")
sc.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, background="white", highlightthickness=0)
background_logo = PhotoImage(file=str(BASE_DIR / "logo.png"))
canvas.create_image(100, 100, image=background_logo)


website_label = Label(text="Website:", bg="white")
email_label = Label(text="Email/Username:", bg="white")
password_label = Label(text="Password:", bg="white")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_frame = Frame(sc, bg="white")
website_entry = Entry(website_frame, bg="white", width=21)
website_entry.focus()
search_button = Button(website_frame, text="Search", bg="white", command=find_data)
website_entry.pack(side="left")
search_button.pack(padx=6, fill="x")

email_entry = Entry(bg="white", width=41)
email_entry.insert(0, "test@test.com")


add_button = Button(text="Add", width=34, bg="white", command=save_data)

password_frame = Frame(sc, bg="white")
password_button = Button(
    password_frame, text="Generate Password", bg="white", command=password_generator
)
password_input = Entry(password_frame, bg="white", width=21)
password_input.pack(side="left")
password_button.pack(padx=6)

canvas.grid(column=1, row=0)
website_frame.grid(column=1, row=1, columnspan=2, sticky="WE")
email_entry.grid(column=1, row=2, columnspan=2, sticky="WE")
password_frame.grid(column=1, row=3, columnspan=2, sticky="WE")
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")


sc.mainloop()
