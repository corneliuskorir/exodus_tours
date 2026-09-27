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
        res = service.add_route(data=data)
        return jsonify(res), 200

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_route(id):
        """get route"""
        route = service.get_route(id=id)
        if route:
            return jsonify(route), 200
        return jsonify({"error": "route not found."}), 404

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_route(id):
        """edit route"""
        data = request.get_json()
        route = service.update(id=id, data=data)
        if route:
            return jsonify(route), 200
        return jsonify({"error": "Route not found"}), 404

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_route(id):
        """Delete route"""
        res = service.delete(id=id)
        if res:
            return jsonify({"message": "Route deleted successfully."}), 204
        return jsonify({"error": "Route not found."})

    return blueprint
