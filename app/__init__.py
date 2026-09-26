from flask import Flask, jsonify

from config import DevelopmentConfig

from .controller import bus_blueprint, route_blueprint, trip_blueprint
from .repository import BusRepository, RouteRepository, TripRepository
from .services import BusService, RouteService, TripService


def create_app(config=None):
    if config == None:
        config = DevelopmentConfig

    app = Flask(__name__)
    app.config.from_object(config)

    if app.config.get("SEED_DATA"):
        # todo: seed data
        pass

    bus_repo = BusRepository()
    route_repo = RouteRepository()
    trip_repo = TripRepository()

    bus_service = BusService(repository=bus_repo)
    route_service = RouteService(repository=route_repo)
    trip_service = TripService(repository=trip_repo)

    app.register_blueprint(bus_blueprint(service=bus_service))
    app.register_blueprint(route_blueprint(service=route_service))
    app.register_blueprint(trip_blueprint(service=trip_service))

    @app.route("/status")
    def server_status():
        return jsonify(
            {"app": __name__, "status": "running", "env": "development"}
        ), 200

    return app
