from tkinter import *
from tkinter import messagebox
from password_generator import gen_pass
import pyperclip
import json

window = Tk()
window.minsize(width=200, height=200)
window.title('Password Manager')
window.config(padx=20, pady=20, highlightthickness=0)


def fill_pass():
    pass_input.delete(0, END)
    new_pass = gen_pass()
    pass_input.insert(0, new_pass)
    pyperclip.copy(new_pass)


def search():
    key = web_input.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not found",
                            message="You haven't save this one")
    else:
        try:
            result = data[key]
        except KeyError:
            messagebox.showinfo(title="Not found",
                                message="You haven't save this one")
        else:
            messagebox.showinfo(
                title=f"{key}", message=f"{result['email']} : {result['pass']}")
    finally:
        print('Search complete')
        web_input.delete(0, END)


def save_data():
    web_data = web_input.get()
    user_data = user_input.get()
    pass_data = pass_input.get()

    new_data = {
        web_data.lower(): {
            "email": user_data,
            "pass": pass_data
        }
    }

    if len(web_data) == 0 or len(pass_data) == 0 or len(user_data) == 0:
        messagebox.showinfo(
            title='Ooopsie', message="All fields must be filled")
    else:
        # confirmed = messagebox.askokcancel(title=web_data,
        #                                    message=f'Is data correct? {web_data} : {user_data} : {pass_data}')
        # if confirmed:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print('Woops,creating your file')
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=2)
        else:
            with open('data.json', 'w') as file:
                data.update(new_data)
                json.dump(data, file, indent=2)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


canvas = Canvas(width=90, height=90)
img = PhotoImage(file='./logo.png')
canvas.create_image(45, 15, image=img)

web_label = Label(text="Website")
user_label = Label(text="eMail/Username")
pass_label = Label(text="Password")
web_input = Entry(width=22)
user_input = Entry(width=45)
pass_input = Entry(width=22)
search_button = Button(text='Search', command=search, width=18)
gen_button = Button(text="Generate Password", width=18, command=fill_pass)
add_button = Button(text="Add", width=38, command=save_data)

canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
pass_label.grid(column=0, row=3)
web_input.grid(column=1, row=1)
search_button.grid(column=2, row=1)
user_input.grid(column=1, row=2, columnspan=2)
pass_input.grid(column=1, row=3)
gen_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

web_input.focus()
user_input.insert(0, 'exampleat@mail.test')
window.mainloop()
