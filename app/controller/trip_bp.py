from flask import Blueprint, jsonify, request


def trip_blueprint():
    """trip blueprint controller"""
    blueprint = Blueprint("trip", __name__, url_prefix="/api/v1/trips")

    @blueprint.route("/", methods=["GET"])
    def get_trips():
        """return list of trips"""
        return jsonify({"message": "Get trip list"}), 200

    @blueprint.route("/", methods=["POST"])
    def add_trip():
        """add new trip"""
        # get trip json data from request
        data = request.get_json()
        # todo: create trip object using data and send to service
        return ("Add new trip", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_trip(id):
        """get trip"""
        # todo: retrieve trip from trip list
        return (f"Get trip using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def edit_trip(id):
        """edit trip"""
        data = request.get_json()
        # todo: use dict to update trip
        return (f"Update trip id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_trip(id):
        """Delete trip"""
        return ("Delete trip", 204)

    # add, remove, list customers ( consider moving to own blueprint)

    @blueprint.route("/<int:id>/passengers", methods=["GET"])
    def get_passengers(id):
        """get passenger list from trip"""
        return jsonify({"message": f"list of passengers in trip id {id}"}), 200

    @blueprint.route("/<int:id>/passengers", methods=["POST"])
    def add_passengers(id):
        """add passenger to trip"""
        data = request.get_json()
        # todo: use data to create passenger and add to trip if seat available
        return (f"Add passenger to trip id {id}", 201)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["GET"])
    def get_passenger(id, pass_id):
        """get passenger"""
        # todo: retrieve trip from trip list
        return (f"Get passenger in trid id {id} of id {pass_id}", 200)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["PATCH"])
    def edit_passenger(id, pass_id):
        """edit passenger"""
        data = request.get_json()
        # todo: use dict to update trip
        return (f"Update passenger in trip id {id} of id {pass_id}", 200)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["DELETE"])
    def delete_passenger(id, pass_id):
        """Delete passenger"""
        return (f"Delete passenger in trip id {id} of {pass_id}", 204)

    return blueprint
