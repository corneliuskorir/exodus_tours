from flask import Blueprint, jsonify, request


def route_blueprint():
    """route blueprint controller"""
    blueprint = Blueprint("route", __name__, url_prefix="/api/v1/routes")

    @blueprint.route("/", methods=["GET"])
    def get_routes():
        """return list of routes"""
        return jsonify({"message": "Get route list"}), 200

    @blueprint.route("/", methods=["POST"])
    def add_route():
        """add new route"""
        # get route json data from request
        data = request.get_json()
        # todo: create route object using data and send to service
        return ("Add new route", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_route(id):
        """get route"""
        # todo: retrieve route from route list
        return (f"Get route using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_route(id):
        """edit route"""
        data = request.get_json()
        # todo: use dict to update route
        return (f"Update route id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_route(id):
        """Delete route"""
        return ("Delete route", 204)

    return blueprint
