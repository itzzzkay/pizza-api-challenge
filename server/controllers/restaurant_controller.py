from flask import Blueprint, jsonify
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import Restaurant_pizza
from server.models import db

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@restaurants_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    restaurant_pizzas = Restaurant_pizza.query.filter_by(restaurant_id=id).all()
    pizzas = [rp.pizza.to_dict() for rp in restaurant_pizzas]
    
    response = restaurant.to_dict()
    response['pizzas'] = pizzas
    return jsonify(response)

@restaurants_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204