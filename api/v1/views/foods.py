#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.store import Store
from models.food import Food
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/stores/<store_id>/foods', methods=['GET'],
                 strict_slashes=False)
def get_fooids(store_id):
    """
    Retrieves the list of all foods objects
    of a specific Store, or a specific food
    """
    list_foods = []
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    for food in store.foods:
        list_foods.append(food.to_dict())

    return jsonify(list_foods)


@app_views.route('/foods/<food_id>/', methods=['GET'], strict_slashes=False)
def get_foods(food_id):
    """
    Retrieves a specific food based on id
    """
    food = storage.get(Food, food_id)
    if not food:
        abort(404)
    return jsonify(food.to_dict())


@app_views.route('/foods/<food_id>', methods=['DELETE'], strict_slashes=False)
def delete_food(food_id):
    """
    Deletes a food based on id provided
    """
    food = storage.get(Food, food_id)

    if not food:
        abort(404)
    storage.delete(food)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/stores/<store_id>/foods', methods=['POST'],
                 strict_slashes=False)
def post_food(store_id):
    """
    Creates a Food
    """
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Food(**data)
    instance.store_id = store.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/foods/<food_id>', methods=['PUT'], strict_slashes=False)
def put_food(food_id):
    """
    Updates a Food
    """
    food = storage.get(Food, food_id)
    if not food:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'store_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(food, key, value)
    storage.save()
    return make_response(jsonify(food.to_dict()), 200)
