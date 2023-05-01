#!/usr/bin/python3
"""index.py"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


hbnbModels = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    stats = {}
    for k, v in hbnbModels.items():
        stats[k] = storage.count(v)
    return jsonify(stats)


if __name__ == "__main__":
    pass
