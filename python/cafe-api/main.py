from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
API_KEY = 'SASAIKUDASAI'

# Cafe TABLE Configuration


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=bool(request.form.get('seats')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=f"£{request.form.get('coffee_price')}",
    )
    db.session.add(new_cafe)
    db.session.commit()
    return render_template("index.html")


@app.route('/search')
def search():
    location = request.args.get('loc')
    data = db.session.query(Cafe).filter_by(location=location)
    cafes = [cafe.to_dict() for cafe in data]
    if not cafes:
        return jsonify({"error": {"Not Found": "Sorry, we don't have anything in this location"}}), 404
    else:
        return jsonify(cafes), 200


@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.form.get('new_price')
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = f"${new_price}"
        db.session.commit()
        return jsonify({"response": "Price update successful"}), 200
    else:
        return jsonify({"error": {"Not Found": "Sorry, we don't have anything in this location"}}), 404


@app.route('/report_closed/<cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    confirm = request.args.get('api_key')
    cafe = db.session.query(Cafe).get(cafe_id)
    print(confirm)
    if cafe and confirm == API_KEY:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"response": "Deleted Successfully"}), 200
    else:
        return jsonify({"error": {"Unauthorized": "You don't have permission to do this"}}), 503


@app.route('/all')
def get_all():
    data = db.session.query(Cafe).all()
    cafes = [cafe.to_dict() for cafe in data]
    return jsonify(cafes), 200


@app.route('/random')
def get_random():
    cafes = db.session.query(Cafe).all()
    cafe = choice(cafes)
    return jsonify(cafe.to_dict()), 200


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
