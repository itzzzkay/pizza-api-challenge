# Pizza Restaurant API

A Flask API for managing a pizza restaurant.

---

##  Setup Instructions

1. **Clone the repo**

```bash
git clone <your-github-repository-url>
cd <your-project-folder>
```

2. **Set up virtual environment with Pipenv**

```bash
pipenv install
pipenv shell
```

3. **Set environment variable for Flask**

```bash
export FLASK_APP=server
```

4. **Run the app**

```bash
flask run
```

##  Database Migration & Seeding

**1. Initialize & migrate DB**

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

**2. Seed data**

```bash
python server/seed.py
```

##  Routes Summary

### GET /pizzas

Returns all pizzas

### POST /pizzas

Creates a new pizza

```json
{
  "name": "Meat Deluxe",
  "ingredients": "Dough, Ham, Chicken, Cheese, Pepperonni"
}
```

### GET /restaurants

Returns all restaurants

### GET /restaurants/\:id

Returns one restaurant with pizzas offered

### DELETE /restaurants/\:id

Deletes a restaurant and all associated RestaurantPizzas

### POST /restaurants

Creates a new restaurant

```json
{
  "name": "Quivers",
  "address": "101 Ngong Road"
}
```

### POST /restaurant_pizzas

Creates a new restaurant pizza (price entry)

```json
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

---

## Validation Rules

### Pizza

- `name` is required and must be unique
- `ingredients` is required

### RestaurantPizza

- `price` must be between 1 and 30
- `pizza_id` and `restaurant_id` must reference valid models

##  Testing with Thunder Client or Postman

- Make sure the server is running
- Use `http://127.0.0.1:5000` as the base URL
- For POST/DELETE requests, use `application/json` header

---

##  Example GET Response

### GET /restaurants/1

```json
{
  "id": 1,
  "name": "Pizza Inn",
  "address": "420 Valley road",
  "pizzas": [
    {
      "id": 1,
      "name": "Plain",
      "ingredients": "Tomato, Dough, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato, Cheese, Pepperoni"
    }
  ]
}
```

---

## Error Response Example

### POST /restaurant_pizzas with invalid price

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```
