from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant_pizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = 
    pizza_id = 