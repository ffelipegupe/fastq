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
