import pandas
import random
from tkinter import *
from tkinter import messagebox

RED = '#ff4d4d'
GREEN = '#70db70'
FONT = ('Courier', 20, 'bold')

langs = ['English', 'Italian', 'French', 'German']

data = pandas.read_csv('top_freq.csv')


def get_data(lang):
    # messagebox.showinfo(title=lang, message=f"{random.choice(data[lang])}")
    idx = random.randint(0, 1000)
    return lang, data[lang][idx], data['Russian'][idx]


def populate_window():
    curr_data = get_data(random.choice(langs))
    print(curr_data)
    # lang_label['text'] = curr_data[0]
    # word_label['text'] = curr_data[1]


window = Tk()
window.minsize(width=600, height=400)
window.title('Flash Cards')

lang_label = Label(text="Language Label", width=20, height=3, font=FONT)
word_label = Label(text="Text Label", width=20, height=3, font=FONT)
yes_button = Button(text="Yes", width=5, height=2,
                    bg=GREEN, command=populate_window)
no_button = Button(text="No", width=5, height=2,
                   bg=RED, command=populate_window)

lang_label.grid(row=1, column=1)
word_label.grid(row=2, column=1)
yes_button.grid(row=3, column=0)
no_button.grid(row=3, column=3)

window.mainloop()
