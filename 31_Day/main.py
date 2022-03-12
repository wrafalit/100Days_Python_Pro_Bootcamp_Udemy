import csv
from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("./data/words_to_learn.csv", mode="r") as file_data:
        df = pandas.read_csv(file_data)

        # print(data)
        df = df.to_dict(orient="records")

except:
    with open("./data/french_words_test.csv", mode="r") as file_data:
        df = pandas.read_csv(file_data)

        # print(data)
        df = df.to_dict(orient="records")
        # print(df)

current_card = {}

# ---------------------------- Funtions ------------------------------- #

def wrong_clic():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card =random.choice(df)
    french_word =current_card["French"]
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_front_view, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front_view, image=card_back)

def right_clic():
    global current_card

    if (len(df)>1):
        df.remove(current_card)
        df_csv = pandas.DataFrame.from_dict(df)
        df_csv.to_csv(r'./data/words_to_learn.csv', index = False, header=True)
        wrong_clic()
    else:
        messagebox.showinfo(title="opss", message="No more words to learn found!\n"
                                                  "It was the last one!")
    # print(df)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=40, pady=40, background=BACKGROUND_COLOR )

flip_timer =window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_front_view=canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400 , 150, text="French", font=("Arial", 30 ,"italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 58, "bold"))

#Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_clic)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_clic)
right_button.grid(column=1,row=1)

wrong_clic()

window.mainloop()