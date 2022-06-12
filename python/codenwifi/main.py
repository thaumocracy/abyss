from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[
                       DataRequired(), Length(min=3, max=20)])
    location = StringField('Location', validators=[DataRequired(), URL()])
    coffee = SelectField('Coffee', choices=[
                        ('0', 'X'), ('1', '☕'), ('2', '☕'), ('3', '☕☕☕'), ('4', '☕☕☕☕'), ('5', '☕☕☕☕☕')])
    wifi = SelectField('Wifi', choices=[
                      ('0', 'X'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'), ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')])
    power = SelectField('Power', choices=[
        ('0', 'X'),  ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('./cafe-data.csv', 'a', encoding='utf-8') as file:
            coffee_data = '☕' * int(form.coffee.data)
            wifi_data = '💪' * int(form.wifi.data)
            power_data = '🔌' * int(form.power.data)
            file.write(
                f'\n{form.cafe.data},{form.location.data},{coffee_data},{wifi_data},{power_data}')
    else:
        print('Error!')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
