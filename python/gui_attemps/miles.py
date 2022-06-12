from tkinter import *

window = Tk()
window.title('Miles to KMs transformer')
window.minsize(height=200, width=400)


def convert():
    res = m_input.get()
    res_label['text'] = round(float(res) / 0.6214, 2)


m_input = Entry()
m_label = Label(text="Miles")
eq_label = Label(text='is equal to')
res_label = Label(text="0")
km_label = Label(text="km")
calc_button = Button(text="Calculate", command=convert)

m_input.grid(column=1, row=0, padx=10)
m_label.grid(column=2, row=0)
eq_label.grid(column=0, row=1)
res_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc_button.grid(column=1, row=2)
window.mainloop()
