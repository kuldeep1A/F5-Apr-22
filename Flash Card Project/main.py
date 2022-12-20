import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
    print(type(original_data))
    print(to_learn)
else:
    to_learn = data.to_dict(orient='records')

# try:
#     data = pandas.read_csv('data/word_to_learn')
# except FileNotFoundError:
#     original_data = pandas.read_csv('data/french_words.csv')
#     to_learn = original_data.to_dict(orient="records")
# else:
#     to_learn = data.to_dict(orient="records")


# print(to_learn)
# print(len(to_learn))


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_know():
    global data
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/word_to_learn.csv', index=False)

    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_know)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()
