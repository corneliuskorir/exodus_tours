from flask import Blueprint, jsonify, request

from ..services import TripService


def trip_blueprint(service: TripService):
    """trip blueprint controller"""
    blueprint = Blueprint("trip", __name__, url_prefix="/api/v1/trips")

    @blueprint.route("/", methods=["GET"])
    def get_trips():
        """return list of trips"""
        all_trips = service.get_all()
        return jsonify(all_trips), 200

    @blueprint.route("/", methods=["POST"])
    def add_trip():
        """add new trip"""
        # get trip json data from request
        data = request.get_json()
        trip = service.add_trip(data=data)
        return ("Add new trip", 201)

    @blueprint.route("/<int:id>", methods=["GET"])
    def get_trip(id):
        """get trip"""
        trip = service.get_trip(id=id)
        return (f"Get trip using id {id}", 200)

    @blueprint.route("/<int:id>", methods=["PATCH"])
    def update_trip(id):
        """edit trip"""
        data = request.get_json()
        trip = service.update_trip(id=id, data=data)
        return (f"Update trip id {id}", 200)

    @blueprint.route("/<int:id>", methods=["DELETE"])
    def delete_trip(id):
        """Delete trip"""
        service.delete_trip(id=id)
        return ("Delete trip", 204)

    # add, remove, list customers ( consider moving to own blueprint)

    @blueprint.route("/<int:id>/passengers", methods=["GET"])
    def get_passengers(id):
        """get passenger list from trip"""
        all_passengers = service.get_passengers(id=id)
        return jsonify({"message": f"list of passengers in trip id {id}"}), 200

    @blueprint.route("/<int:id>/passengers", methods=["POST"])
    def add_passengers(id):
        """add passenger to trip"""
        data = request.get_json()
        passenger = service.add_passenger(data=data)
        return (f"Add passenger to trip id {id}", 201)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["GET"])
    def get_passenger(id, pass_id):
        """get passenger"""
        passenger = service.get_passenger(id=id, pass_id=pass_id)
        return (f"Get passenger in trid id {id} of id {pass_id}", 200)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["PATCH"])
    def edit_passenger(id, pass_id):
        """edit passenger"""
        data = request.get_json()
        passenger = service.update_passenger(id=id, pass_id=pass_id, data=data)
        return (f"Update passenger in trip id {id} of id {pass_id}", 200)

    @blueprint.route("/<int:id>/passengers/<int:pass_id>", methods=["DELETE"])
    def delete_passenger(id, pass_id):
        """Delete passenger"""
        service.delete_passenger(id=id, pass_id=pass_id)
        return (f"Delete passenger in trip id {id} of {pass_id}", 204)

    return blueprint
