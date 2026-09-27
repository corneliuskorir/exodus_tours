from flask import Blueprint, jsonify, request

from ..services import RouteService


def route_blueprint(service: RouteService):
    """route blueprint controller"""
    blueprint = Blueprint("route", __name__, url_prefix="/api/v1/routes")

    @blueprint.route("/", methods=["GET"])
    def get_routes():
        """return list of routes"""
        all_routes = service.get_all()
        return jsonify(all_routes), 200

    @blueprint.route("/", methods=["POST"])
    def add_route():
        """add new route"""
        # get route json data from request
        data = request.get_json()
        route = service.add_route(data=data)
        return ("Add new route", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_route(id):
        """get route"""
        route = service.get_route(id=id)
        return (f"Get route using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_route(id):
        """edit route"""
        data = request.get_json()
        route = service.update(id=id, data=data)
        return (f"Update route id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_route(id):
        """Delete route"""
        service.delete(id=id)
        return ("Delete route", 204)

    return blueprint
