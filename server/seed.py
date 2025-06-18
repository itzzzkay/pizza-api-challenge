from server.app import app
from server.models.pizza import db, Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import Restaurant_pizza

def seed_database():
    with app.app_context():

        print("Deleting existing data...")
        Restaurant_pizza.query.delete()
        Pizza.query.delete()
        Restaurant.query.delete()

        print("Seeding Pizzas...")

        plain = Pizza(name="Plain", ingredients="Dough, Tomato Sauce, Cheese")
        hawaiian = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Pineapple, Ham")
        pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        veggie = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Veggies")

        db.session.add_all([plain, hawaiian, pepperoni, veggie])
        db.session.commit()

        print("Seeding Restaurants...")

        dominos = Restaurant(name="Dominos", address="Junction Mall")
        pizza_hut = Restaurant(name="Pizza hut", address="Garden City Mall")
        papa_johns = Restaurant(name="Papa Johns", address="Diamond Plaza")

        db.session.add_all([dominos, pizza_hut, papa_johns])
        db.session.commit()

        print("Seeding RestaurantPizzas...")

        RP1 = Restaurant_pizza(price=12, restaurant=dominos, pizza=plain)
        RP2 = Restaurant_pizza(price=17, restaurant=pizza_hut, pizza=veggie)
        RP3 = Restaurant_pizza(price=14, restaurant=papa_johns, pizza=pepperoni)
        RP4 = Restaurant_pizza(price=20, restaurant=dominos, pizza=hawaiian)

        db.session.add_all([RP1, RP2, RP3, RP4])
        db.session.commit()

if __name__ == "__main__":
    seed_database()
