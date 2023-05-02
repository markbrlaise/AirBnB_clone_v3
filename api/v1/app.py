#!/usr/bin/python3
"""our app.py to connect to """

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    """method to close session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """404 page not found"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', '5000'), threaded=True)
