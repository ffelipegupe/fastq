#!/usr/bin/python3
""" Objects that handle all default RestFul API actions for drinks """
from models.store import Store
from models.drink import Drink
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/stores/<store_id>/drinks', methods=['GET'],
                 strict_slashes=False)
def get_drinkids(store_id):
    """
    Retrieves the list of all drink objects
    of a specific Store, or a specific food
    """
    list_drinks = []
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    for drink in store.drinks:
        list_drinks.append(drink.to_dict())

    return jsonify(list_drinks)


@app_views.route('/drinks/<food_id>/', methods=['GET'], strict_slashes=False)
def get_drinks(drink_id):
    """
    Retrieves a specific drink based on id
    """
    drink = storage.get(drink, drink_id)
    if not drink:
        abort(404)
    return jsonify(drink.to_dict())


@app_views.route('/drinks/<drink_id>', methods=['DELETE'], strict_slashes=False)
def delete_drink(drink_id):
    """
    Deletes a drink based on id provided
    """
    drink = storage.get(Drink, drink_id)

    if not drink:
        abort(404)
    storage.delete(drink)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/stores/<store_id>/drinks', methods=['POST'],
                 strict_slashes=False)
def post_drink(store_id):
    """
    Creates a drink
    """
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Drink(**data)
    instance.store_id = store.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/foods/<drink_id>', methods=['PUT'], strict_slashes=False)
def put_drink(drink_id):
    """
    Updates a Drink
    """
    drink = storage.get(Drink, drink_id)
    if not drink:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'store_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(drink, key, value)
    storage.save()
    return make_response(jsonify(drink.to_dict()), 200)
