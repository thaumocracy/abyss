from tkinter import *
from quiz_brain import QuizBrain

THEME = '#4d004d'
FONT = ('Arial', 12, 'italic')


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME)
        self.score = Label(text='Score : 0', fg='white', bg=THEME)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text='Some RYBA text for now', fill=THEME,
                                                font=FONT)
        yes_image = PhotoImage(file='./img/yes.png')
        self.yes_btn = Button(image=yes_image, highlightthickness=0, command=self.press_true)
        no_image = PhotoImage(file='./img/no.png')
        self.no_btn = Button(image=no_image, highlightthickness=0, command=self.press_false)
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.yes_btn.grid(row=2, column=0)
        self.no_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text='You finished this quiz!')
            self.yes_btn.config(state='disabled')
            self.no_btn.config(state='disabled')

    def press_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
        self.score['text'] = f"Score: {self.quiz.score}"

    def press_false(self):
        self.give_feedback(self.quiz.check_answer('False'))
        self.score['text'] = f"Score: {self.quiz.score}"

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#80ffaa")
        else:
            self.canvas.config(bg="#ff9980")
        self.window.after(1000, self.get_next_question)
