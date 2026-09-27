from flask import Blueprint, jsonify, request

from ..services import BusService


def bus_blueprint(service: BusService):
    """Bus blueprint controller"""
    blueprint = Blueprint("bus", __name__, url_prefix="/api/v1/buses")

    @blueprint.route("/", methods=["GET"])
    def get_buses():
        """return list of buses"""
        bus_list = service.get_all()
        return jsonify(bus_list), 200

    @blueprint.route("/", methods=["POST"])
    def add_bus():
        """add new bus"""
        # get bus json data from request
        data = request.get_json()
        bus = service.add_bus(data)
        return ("Add new bus", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_bus(id):
        """get bus"""
        bus = service.get_bus(id)
        return (f"Get bus using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_bus(id):
        """edit bus"""
        data = request.get_json()
        bus = service.update(id, data)
        return (f"Update bus id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_bus(id):
        """Delete bus"""
        service.delete(id)
        return ("Delete bus", 204)

    return blueprint
