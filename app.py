from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/wewes_bite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -------------------
# Database Models
# -------------------

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    description = db.Column(db.String(300))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    total_price = db.Column(db.Float)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    item_price = db.Column(db.Float)

# -------------------
# Routes
# -------------------

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def menu():
    products = Product.query.all()
    return render_template("menu.html", products=products)

@app.route("/admin")
def admin_dashboard():
    products = Product.query.all()
    return render_template("admin_dashboard.html", products=products)

# -------------------
# Run App
# -------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create database tables if not exist
    app.run(debug=True)
