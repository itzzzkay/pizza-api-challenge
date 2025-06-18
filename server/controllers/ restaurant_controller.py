from flask import Blueprint, jsonify
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza
from ..app import db

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()
    pizzas = [rp.pizza.to_dict() for rp in restaurant_pizzas]
    
    response = restaurant.to_dict()
    response['pizzas'] = pizzas
    return jsonify(response)

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204