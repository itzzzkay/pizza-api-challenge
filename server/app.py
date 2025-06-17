from flask import Flask
from flask_migrate import Migrate
from .models.pizza import db, Pizza
from .models.restaurant import db, Restaurant
from .models.restaurant_pizza import db, Restaurant_pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa.db'

migrate = Migrate(app, db)
db.init_app(app)