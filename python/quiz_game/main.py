from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

from quiz_interface import *

def get_questions(data):
    arr = []
    for item in data:
        arr.append(Question(item["text"], item["answer"]))
    return arr


question_bank = get_questions(question_data)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()


print(f'Great job! Your final score is {quiz.score}/{len(quiz.question_list)}')
