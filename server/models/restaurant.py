from . import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('Restaurant_pizza', backref='restaurant', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }