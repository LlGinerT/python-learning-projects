import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=15, pady=10)


my_label = tk.Label(text="First label", font=("Arial", 24, "bold"))
# my_label.pack()  # stacks the components on the side we select, default 'center'
# my_label.place(x=0,y=0) specific place on the screen, starting on top left corner
my_label.grid(
    column=0, row=0
)  # imaginary grid based on all components added to the grid
# for change config of Label(dict)
my_label["text"] = "like dictionary"
my_label.config(text="with config method", padx=25, pady=40)


# Button
clicks = 0


def button_clicked():
    global clicks
    clicks += 1
    my_label.config(text=f"Click {clicks}")


button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)


def input_print():
    my_label.config(text=input.get())
    input.delete(0, tk.END)


# Entry

input = tk.Entry(width=10)
input.grid(column=0, row=2)

print_button = tk.Button(text="print", command=input_print)
print_button.grid(column=0, row=3)
window.mainloop()
