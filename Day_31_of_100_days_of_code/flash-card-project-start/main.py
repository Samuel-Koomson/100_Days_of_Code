import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
VINTAGE_COLOR = "#6F4C5B"
BROWN_COLOR = "#9E7777"
BIEGE_COLOR = "#DEBA9D"
YELLOW_COLOR = "#F5E8C7"

# ---------------------------- READING FROM DATA FILES ------------------------------- #
displayed_card = {}
study_words = {}

try:
    words_data = pandas.read_csv("./data/french_words.csv")
# print(words_data)
except FileNotFoundError:
    source_data = pandas.read_csv("./data/french_words.csv")
    study_words = source_data.to_dict(orient="records")
else:
    study_words = words_data.to_dict(orient="records")



def incumbent_word():
    global displayed_card, flip_time
    card_console.after_cancel(flip_time)
    displayed_card = random.choice(study_words)
    canvas.itemconfig(title_text, text="French", fill='black')
    canvas.itemconfig(current_word, text=displayed_card["French"], fill='black')
    canvas.itemconfig(canvas_background, image=front_card)
    flip_time = card_console.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill='white')
    canvas.itemconfig(current_word, text=displayed_card["English"], fill='white')
    canvas.itemconfig(canvas_background, image=back_card)


def known_words():
    study_words.remove(displayed_card)
    incumbent_word()
    new_data = pandas.DataFrame(study_words)
    new_data.to_csv("./data/unknown_words", index=False)
    incumbent_word()


# ---------------------------- UI SETUP ------------------------------- #
card_console = Tk()
card_console.title("FLASH CARD CAPSTONE PROJECT")
card_console.config(width=850, height=800, padx=5, pady=5, bg=BIEGE_COLOR)


flip_time = card_console.after(3000, func=flip_card)

#the next 5 lines below and and customizes the canvas
canvas = Canvas(width=800, height=526) #card canvas
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
canvas_background = canvas.create_image(400, 263, image=front_card)

# canvas.create_image(400, 263, image=back_card)

title_text = canvas.create_text(400, 150, text='French', font=('Ariel', 30, 'italic'))
current_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 40, 'bold'))
canvas.config(bg=BIEGE_COLOR, highlightthickness=0)
canvas.place(x=20, y=20)

skip_card = PhotoImage(file='./images/wrong.png')
skip_card_button = Button(width=70, height=70, image=skip_card, command=incumbent_word)
skip_card_button.place(x=200, y=560)

correct_answer = PhotoImage(file='./images/right.png')
correct_answer_button = Button(width=70, height=70, image=correct_answer, command=known_words)
correct_answer_button.place(x=550, y=560)

# flash_card = Canvas(width=800, height=526) #card canvas
# back_card = PhotoImage(file='./images/card_back.png')
# flash_card.create_image(400, 263, image=back_card)

# work_check = flash_card.create_text(400, 150, text='FRENCH', font=('Ariel', 30, 'italic'))
# verified_word = flash_card.create_text(400, 263, text='correct word', font=('Ariel', 40, 'bold'))


incumbent_word()
# flip_card()
card_console.mainloop()
