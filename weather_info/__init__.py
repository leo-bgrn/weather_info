from flask import Flask, jsonify
from flask_restx import Api

from weather_info.params.params import config_by_name
from .api.location.location_controller import api as location_api
from .api.forecast.forecast_controller import api as weather_api


def create_app(env=None):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Flaskerific API", version="0.1.0")

    api.add_namespace(location_api, path=f"/api/location")
    api.add_namespace(weather_api, path=f"/api/forecast")

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
