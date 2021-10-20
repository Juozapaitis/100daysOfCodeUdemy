from tkinter import *
import pandas
import random
import time
from gtts import gTTS
import os
import playsound

BACKGROUND_COLOR = "#B1DDC6"
PATH_TO_CARD_FRONT = "100 days of code//day 31//images//card_front.png"
PATH_TO_CARD_BACK = "100 days of code//day 31//images//card_back.png"
PATH_TO_RIGHT = "100 days of code//day 31//images//right.png"
PATH_TO_WRONG = "100 days of code//day 31//images//wrong.png"
FONT_LANGUAGE = ('Arial', 40, 'italic')
FONT_WORD = ('Arial', 60, 'bold')
PATH_TO_DATA = "100 days of code//day 31//data//french_words.csv"
PATH_TO_WORDS_TO_LEARN = "100 days of code//day 31//data//words_to_learn.csv"

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv(PATH_TO_WORDS_TO_LEARN)
except FileNotFoundError:
    original_data = pandas.read_csv(PATH_TO_DATA)
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records")
    

def next_card():
    language = 'fr'
    global current_card, flip_timer
    
    current_card = random.choice(to_learn)
    selected_card = current_card["French"]
    window.after_cancel(flip_timer)
    canvas.itemconfig(language_text, text = "French", fill = "black")
    canvas.itemconfig(word_text, text = selected_card, fill = "black")
    canvas.itemconfig(card_background, image = front_img)
    window.after(100)
    audio_output = gTTS(text=selected_card, lang = language)
    audio_output.save("english_word.mp3")
    playsound.playsound("english_word.mp3", True)
    os.remove("english_word.mp3")
    flip_timer = window.after(3000, func=turn_card)

def turn_card():
    language = 'en'
    selected_card = current_card["English"]
    canvas.itemconfig(card_background, image = turned_img)
    canvas.itemconfig(language_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, text = selected_card, fill = "white")
    audio_output = gTTS(text=current_card["English"], lang = language)
    audio_output.save("french_word.mp3")
    playsound.playsound("french_word.mp3", True)
    os.remove("french_word.mp3")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(PATH_TO_WORDS_TO_LEARN, index=False)
    next_card()

window = Tk()
window.title("Flash card")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=turn_card)

canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
turned_img = PhotoImage(file = PATH_TO_CARD_BACK)
front_img = PhotoImage(file = PATH_TO_CARD_FRONT)

card_background = canvas.create_image(400, 263, image=front_img)

language_text = canvas.create_text(400, 150, text = "French", font = FONT_LANGUAGE)
word_text = canvas.create_text(400, 263, text = "trouve", font = FONT_WORD)

canvas.grid(column = 0, row = 0, columnspan = 2)

right_image = PhotoImage(file=PATH_TO_RIGHT)
right_button = Button(image=right_image, highlightthickness=0, command =is_known)
right_button.grid(column = 1, row = 1)

wrong_image = PhotoImage(file=PATH_TO_WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0, command = next_card)
wrong_button.grid(column = 0, row = 1)

next_card()

window.mainloop()