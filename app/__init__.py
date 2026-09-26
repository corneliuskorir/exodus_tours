from flask import Flask, jsonify

from config import DevelopmentConfig

from .controller import bus_blueprint, route_blueprint, trip_blueprint
from .services import BusService, RouteService, TripService


def create_app(config=None):
    if config == None:
        config = DevelopmentConfig

    app = Flask(__name__)
    app.config.from_object(config)

    if app.config.get("SEED_DATA"):
        # todo: seed data
        pass

    bus_service = BusService()
    route_service = RouteService()
    trip_service = TripService()

    app.register_blueprint(bus_blueprint(service=bus_service))
    app.register_blueprint(route_blueprint(service=route_service))
    app.register_blueprint(trip_blueprint(service=trip_service))

    @app.route("/status")
    def server_status():
        return jsonify(
            {"app": __name__, "status": "running", "env": "development"}
        ), 200

    return app
