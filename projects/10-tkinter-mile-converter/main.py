from tkinter import *

sc = Tk()
sc.title("Distance converter")
sc.config(padx=20, pady=20)

input_label = Label(text="Input: ")
input_label.grid(column=0, row=0)
output_label = Label(text="is equal to: ")
output_label.grid(column=0, row=1)

input_unit = Label(text="Km")
input_unit.grid(column=2, row=0)
output_unit = Label(text="Miles")
output_unit.grid(column=2, row=1)

user_input = Entry(width=10)
user_input.insert(0, "0")
user_input.select_range(start=0, end=END)
user_input.focus()
user_input.grid(column=1, row=0)

conversion_output = Label(text="0")
conversion_output.grid(column=1, row=1)

km_miles_var = IntVar(value=1)
miles_km_var = IntVar(value=0)


def km_to_miles():
    miles_km_var.set(0)
    input_unit.config(text="km")
    output_unit.config(text="Miles")


def miles_to_km():
    km_miles_var.set(0)
    input_unit.config(text="Miles")
    output_unit.config(text="Km")


km_miles_check = Checkbutton(
    text="Km to Miles", command=km_to_miles, variable=km_miles_var
)
km_miles_check.select()
km_miles_check.grid(column=0, row=3)
miles_km_check = Checkbutton(
    text="Miles to Km", command=miles_to_km, variable=miles_km_var
)
miles_km_check.grid(column=0, row=4)


def conversion_logic():
    num = float(user_input.get())
    if km_miles_var.get() == 1:
        result = num * 0.621371
    elif miles_km_var.get() == 1:
        result = num / 0.621371
    conversion_output.config(text=f"{result:.3f}")
    user_input.select_range(start=0, end=END)
    user_input.focus()


calculate = Button(text="Calculate", command=conversion_logic)
calculate.grid(column=1, row=3)
sc.mainloop()
