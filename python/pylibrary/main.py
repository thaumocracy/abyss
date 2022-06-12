from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


all_books = []

# #Unix/Mac (note the four leading slashes)
# sqlite:////absolute/path/to/foo.db
# #Windows (note 3 leading forward slashes and backslash escapes)
# sqlite:///C:\\absolute\\path\\to\\foo.db
# #Windows (alternative using raw string)
# r'sqlite:///C:\absolute\path\to\foo.db'


@app.route('/')
def home():
    data = Books.query.all()
    return render_template('index.html', books=data)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        book_author = request.form.get('book_author')
        book_rating = request.form.get('book_rating')
        new_db_book = Books(
            title=book_name, author=book_author, rating=book_rating)
        db.session.add(new_db_book)
        db.session.commit()
    return render_template('add.html')

# TODO Check this again


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)
# TODO Check this again


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
