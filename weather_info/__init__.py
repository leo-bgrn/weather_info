from flask import Flask, jsonify
from flask_restx import Api

from weather_info.params.config import config_by_name


def create_app(env=None):

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Flaskerific API", version="0.1.0")

    #register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app