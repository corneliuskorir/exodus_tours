from flask import Flask, jsonify

from config import DevelopmentConfig


def create_app(config=None):
    if config == None:
        config = DevelopmentConfig

    app = Flask(__name__)
    app.config.from_object(config)

    if app.config.get("SEED_DATA"):
        # todo: seed data
        pass

    @app.route("/status")
    def server_status():
        return jsonify(
            {"app": __name__, "status": "running", "env": "development"}
        ), 200

    return app
