from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import Restaurant_pizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models import db

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    

    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
        price = int(data['price'])
        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    except ValueError:
        return jsonify({"errors": ["Price must be a valid integer"]}), 400
    
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    
    if not pizza or not restaurant:
        return jsonify({"errors": ["Pizza or Restaurant not found"]}), 404

    restaurant_pizza = Restaurant_pizza(
        price=price,
        pizza_id=data['pizza_id'],
        restaurant_id=data['restaurant_id']
    )
    
    db.session.add(restaurant_pizza)
    db.session.commit()
    
    return jsonify(restaurant_pizza.to_dict()), 201