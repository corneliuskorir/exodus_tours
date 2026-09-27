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
        data = request.get_json()

        return service.add_bus(data), 201

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_bus(id):
        """get bus"""
        res = service.get_bus(id)
        if res:
            return jsonify(res), 200
        return jsonify({"error": "Bus not found"}), 404

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_bus(id):
        """edit bus"""
        data = request.get_json()
        res = service.update(id, data)
        if res:
            return jsonify(res), 200
        return jsonify({"error": "Bus not found"}), 404

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_bus(id):
        """Delete bus"""
        res = service.delete(id)
        if res:
            return jsonify({"message": "Bus deleted successfully"}), 204
        return jsonify({"error": "Bus not found"}), 404

    return blueprint
