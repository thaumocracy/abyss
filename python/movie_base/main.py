from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(4), nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)


class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    year = StringField('Release year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Your movie rating', validators=[DataRequired()])
    review = StringField('Your movie review', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired(), URL()])
    submit = SubmitField('Add')


class MovieEditForm(FlaskForm):
    rating = StringField('Your movie rating', validators=[DataRequired()])
    submit = SubmitField('Edit')


@ app.route("/")
def home():
    data = Movie.query.order_by(Movie.rating).all()
    return render_template("index.html", movies=data)


@ app.route('/add', methods=['GET', 'POST'])
def add_movie():
    myForm = MovieForm()
    if request.method == 'POST':
        mov = Movie(title=myForm.title.data, year=myForm.year.data, description=myForm.description.data,
                    rating=myForm.rating.data, review=myForm.review.data, img_url=myForm.img_url.data)
        db.session.add(mov)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=myForm)


@ app.route('/delete')
def delete_movie():
    movie = Movie.query.get(request.args.get('id'))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@ app.route('/edit', methods=['GET', 'POST'])
def edit_movie():
    myForm = MovieEditForm()
    if request.method == 'POST':
        movie_id = request.form["id"]
        current_movie = Movie.query.get(movie_id)
        rating = request.args.get('rating')
        current_movie.rating = myForm.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_selected)


if __name__ == '__main__':
    app.run(debug=True)
