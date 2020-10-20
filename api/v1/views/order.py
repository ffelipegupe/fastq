#!/usr/bin/python3
""" Objects that handle all default RestFul API actions for orders """
from models.order import Order
from models.food import Food
from models.drink import Drink
from models.store import Store
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/stores/<store_id>/orders', methods=['GET'],
                 strict_slashes=False)
def get_orderids(store_id):
    """
    Retrieves the list of all order objects
    of a specific Store, or a specific Store
    """
    list_orders = []
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    for order in store.orders:
        list_orders.append(order.to_dict())

    return jsonify(list_orders)

@app_views.route('/orders/<order_id>/', methods=['GET'], strict_slashes=False)
def get_orders(order_id):
    """
    Retrieves a specific order based on id
    """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)
    return jsonify(order.to_dict())


@app_views.route('/orders/<order_id>', methods=['DELETE'], strict_slashes=False)
def delete_order(order_id):
    """
    Deletes an order based on id provided
    """
    order = storage.get(Order, order_id)

    if not order:
        abort(404)
    storage.delete(order)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/store/<store_id>/orders', methods=['POST', 'GET'],
                 strict_slashes=False)
def post_order(store_id):
    """
    Creates an Order to a Store
    """
    store = storage.get(Store, store_id)
    if not store:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'order_number' not in request.get_json():
        abort(400, description="Missing order number")
    if 'user_name' not in request.get_json():
        abort(400, description="Missing user name")

    data = request.get_json()
    instance = Order(**data)
    instance.store_id = store.id
    instance.order_number = request.get_json(['order_number'])
    instance.phone = request.get_json(['phone'])
    instance.units = request.get_json(['units'])
    instance.total = request.get_json(['total'])
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
def put_order(order_id):
    """
    Updates an Order
    """
    order = storage.get(Order, order_id)
    if not order:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'store_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(order, key, value)
    storage.save()
    return make_response(jsonify(food.to_dict()), 200)
