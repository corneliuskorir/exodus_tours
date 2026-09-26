from flask import Blueprint, jsonify, request


def bus_blueprint():
    """Bus blueprint controller"""
    blueprint = Blueprint("bus", __name__, url_prefix="/api/v1/buses")

    @blueprint.route("/", methods=["GET"])
    def get_buses():
        """return list of buses"""
        return jsonify({"message": "Get bus list"}), 200

    @blueprint.route("/", methods=["POST"])
    def add_bus():
        """add new bus"""
        # get bus json data from request
        data = request.get_json()
        # todo: create bus object using data and send to service
        return ("Add new bus", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_bus(id):
        """get bus"""
        # todo: retrieve bus from bust list
        return (f"Get bus using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_bus(id):
        """edit bus"""
        data = request.get_json()
        # todo: use dict to update bus
        return (f"Update bus id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_bus(id):
        """Delete bus"""
        return ("Delete bus", 204)

    return blueprint
