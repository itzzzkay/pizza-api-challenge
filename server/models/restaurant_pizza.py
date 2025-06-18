from . import db

class Restaurant_pizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza": self.pizza.to_dict() if self.pizza else None
        }