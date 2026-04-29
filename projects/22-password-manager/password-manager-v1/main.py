from pathlib import Path
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

BASE_DIR = Path(__file__).parent

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
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    fields = {"Website": website, "Email": email, "Password": password}
    empty_fields = {
        field: entry for (field, entry) in fields.items() if len(fields[field]) == 0
    }

    if len(empty_fields) == 0:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Email: {email}\nPassword: {password}\nDo you want save?",
        )
        if is_ok:
            with open(BASE_DIR / "passwords.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")

        website_input.delete(0, END)
        email_input.delete(0, END)
        email_input.insert(0, "test@test.com")
        password_input.delete(0, END)
        website_input.focus()
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


website_input = Entry(bg="white", width=41)
website_input.focus()
email_input = Entry(bg="white", width=41)
email_input.insert(0, "test@test.com")


add_button = Button(text="Add", width=34, bg="white", command=save_data)

password_frame = Frame(sc, bg="white")
password_button = Button(
    password_frame, text="Generate Password", bg="white", command=password_generator
)
password_input = Entry(password_frame, bg="white", width=21)
password_input.pack(side="left")
password_button.pack(padx=6)

canvas.grid(column=1, row=0)
website_input.grid(column=1, row=1, columnspan=2, sticky="WE")
email_input.grid(column=1, row=2, columnspan=2, sticky="WE")
password_frame.grid(column=1, row=3, columnspan=2, sticky="WE")
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")


sc.mainloop()
