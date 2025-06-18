from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.models.restaurant import  Restaurant
from server.models.restaurant_pizza import Restaurant_pizza
from server.controllers.restaurant_controller import restaurants_bp
from server.controllers.pizza_controller import pizzas_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp



migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(restaurants_bp, url_prefix="/restaurants")
    app.register_blueprint(pizzas_bp, url_prefix="/pizzas")
    app.register_blueprint(restaurant_pizzas_bp, url_prefix="/restaurant_pizzas")

    return app