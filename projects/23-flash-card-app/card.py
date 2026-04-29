from random import choice
from tkinter import Canvas, PhotoImage
from constants import BACKGROUND_COLOR, IMAGE_DIR


class Card(Canvas):
    def __init__(self):
        super().__init__(
            height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0
        )
        self.card_image_front = PhotoImage(file=str(IMAGE_DIR / "card_front.png"))
        self.card_image_back = PhotoImage(file=str(IMAGE_DIR / "card_back.png"))
        self.card_background = self.create_image(400, 263, image=self.card_image_front)
        self.card_tittle = self.create_text(
            400, 150, text="Test", font=("Ariel", 40, "italic")
        )
        self.card_word = self.create_text(
            400, 263, text="Test", font=("Ariel", 60, "bold")
        )
        self._word = ""

    def update_card(self, word, language, color):
        self.itemconfig(self.card_tittle, text=language, fill=color)
        self.itemconfig(self.card_word, text=word, fill=color)

    def new_word(self, words_dict):
        self._word = choice(words_dict)
        self.update_card(word=self._word["French"], language="French", color="black")
        self.itemconfig(self.card_background, image=self.card_image_front)

    def flip_card(self):
        self.update_card(word=self._word["English"], language="English", color="white")
        self.itemconfig(self.card_background, image=self.card_image_back)

    def word(self):
        return self._word
