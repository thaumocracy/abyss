from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)

years = f"1970 - {dt.datetime.now().year}"


@app.route('/')
def index():
    return render_template('index.html', data=years)


if __name__ == '__main__':
    app.run(debug=True)
