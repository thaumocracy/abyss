from flask import Flask
import random

app = Flask(__name__)

choice = random.randint(1, 10)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/<num>')
def check_num(num):
    user_input = int(num)
    if user_input == choice:
        return f'You guessed,its {user_input}'
    elif user_input > choice:
        return f'{user_input} is too high,fella'
    else:
        return f'{user_input} is too low,fella'


if __name__ == '__main__':
    app.run(debug=True)
