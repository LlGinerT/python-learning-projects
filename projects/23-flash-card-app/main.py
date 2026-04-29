from tkinter import *
from constants import *
from card import *
import pandas as pd


root = Tk()
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.title("Flash Cards")
try:
    df = pd.read_csv(TO_LEARN_PATH)
except FileNotFoundError:
    df = pd.read_csv(DATA_PATH)
words_dict = df.to_dict(orient="records")


# Card config
card = Card()
card.grid(column=0, row=0, columnspan=2)

flip_timer_id = None


def right_logic():
    global words_dict
    word_to_remove = card.word()
    if word_to_remove in words_dict:
        words_dict.remove(word_to_remove)
    next_card()


def next_card():
    global flip_timer_id
    global words_dict
    if flip_timer_id:
        root.after_cancel(flip_timer_id)
    try:
        card.new_word(words_dict)
    except Exception as e:
        print(f"error:{e}")
        df = pd.read_csv(DATA_PATH)
        words_dict = df.to_dict(orient="records")
        card.new_word(words_dict)
    flip_timer_id = root.after(3000, card.flip_card)


# Buttons config
wrong_image = PhotoImage(file=str(IMAGE_DIR / "wrong.png"))
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
right_image = PhotoImage(file=str(IMAGE_DIR / "right.png"))
right_button = Button(
    image=right_image, highlightthickness=0, bd=0, command=right_logic
)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

next_card()


root.mainloop()

# Save on_close
new_df = pd.DataFrame(words_dict)
new_df.to_csv(TO_LEARN_PATH, index=False)
