from tkinter import *
import requests

window = Tk()
window.minsize(width=300, height=300)
window.title('Kanye speaks:')
window.config(padx=50, pady=50)


def get_quote():
    data = requests.get('http://api.kanye.rest/').json()
    quote = data['quote']
    quote_label['text'] = quote


quote_label = Label(text="The quote", font=('Courier', 20, 'bold'))
next_button = Button(text="Get another", command=get_quote)

quote_label.grid(row=1, column=1)
next_button.grid(row=2, column=1)
window.mainloop()
