from pathlib import Path
from tkinter import *
from constants import *

reps = 0
timer = None
BASE_DIR = Path(__file__).parent


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    sc.after_cancel(timer)
    check_label["text"] = ""
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    start_button.config(text="Start", command=timer_start)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    start_button.config(text="Stop", command=reset_timer)
    global reps
    reps += 1
    if reps % 2 != 0:
        print(f"work time {reps}")
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        print(f"long rest time {reps}")
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        print(f"short rest time {reps}")
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = sc.after(1000, count_down, count - 1)
    else:
        timer_start()
        if reps % 2 == 0:
            if len(check_label["text"]) % 4 == 0 and len(check_label["text"]) != 0:
                check_label["text"] += "\n"
            check_label["text"] += "✔"
    # start_button.config(state="normal")


# ---------------------------- UI SETUP ------------------------------- #
sc = Tk()
sc.title("Pomodoro")
sc.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_img = PhotoImage(file=str(BASE_DIR / "tomato.png"))
canvas.create_image(100, 112, image=background_img)
timer_text = canvas.create_text(
    100,
    130,
    fill="white",
    font=(FONT_NAME, 30, "bold"),
)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
check_label = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)


start_button = Button(text="Start", highlightthickness=0, command=timer_start)
# reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)


title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=2, row=2)
# reset_button.grid(column=2, row=2)
check_label.grid(column=1, row=3)

sc.mainloop()
