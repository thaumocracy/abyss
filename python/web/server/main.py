from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/')
def index(username=None):
    return render_template('index.html')


@app.route('/<string:page_name>')
def gen_link(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/test.html')
        except:
            return 'Database error'
    else:
        return 'Bip-bop everything is fked'
