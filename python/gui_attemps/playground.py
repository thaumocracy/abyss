from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
state = 1
MARK = '✔'


def start_timer():
    global state
    state += 1
    marks['text'] = f"{MARK * state}"
    print(f'TIMER IS GOING for {state} time')


def reset_timer():
    global state
    state = 0
    print('Im doing da reset')


window = Tk()
window.minsize(height=400, width=400)
window.config(padx=100, pady=100, bg=YELLOW, highlightthickness=0)
window.title('Pomodoro Tkinter GUI')

canvas = Canvas(width=235, height=215)
img = PhotoImage(file='./tomato.png')
canvas.create_image(115, 110, image=img)
canvas.create_text(115, 135, text="00:00", fill="white",
                   font=(FONT_NAME, 32, 'bold'))
text = Label(text="Working", fg=PINK, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
button_start = Button(text="Start", bg=GREEN, fg=YELLOW, padx=10, pady=10, font=(FONT_NAME, 16, 'bold'),
                      command=start_timer)
button_reset = Button(text="Reset", bg=GREEN, fg=YELLOW, padx=10, pady=10, font=(FONT_NAME, 16, 'bold'),
                      command=reset_timer)
marks = Label(text=f"{MARK * state}", fg=GREEN,
              bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)
text.grid(column=1, row=2)
button_start.grid(column=0, row=3)
button_reset.grid(column=2, row=3)
marks.grid(column=1, row=3)
window.mainloop()
