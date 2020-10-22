#!/usr/bin/python3
from models.store import Store
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/stores', methods=['GET'], strict_slashes=False)
def get_stores():
    """
    Retrieves the list of all Store objects
    """
    all_stores = storage.all(Store).values()
    list_stores = []
    for store in all_stores:
        list_stores.append(store.to_dict())
    return jsonify(list_stores)

@app_views.route('/stores/<store_id>', methods=['GET'], strict_slashes=False)
def get_store(store_id):
    """ Retrieves a specific Store """
    store = storage.get(Store, store_id)
    if not store:
        abort(404)

    return jsonify(store.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_store(store_id):
    """
    Deletes a Store Object
    """

    store = storage.get(Store, store_id)

    if not store:
        abort(404)

    storage.delete(store)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/stores', methods=['POST'], strict_slashes=False)
def post_store():
    """
    Creates a Store
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Store(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/stores/<store_id>', methods=['PUT'], strict_slashes=False)
def put_store(store_id):
    """
    Updates a Store
    """
    store = storage.get(Store, store_id)

    if not store:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(store, key, value)
    storage.save()
    return make_response(jsonify(store.to_dict()), 200)
