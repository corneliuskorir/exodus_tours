from dataclasses import asdict, dataclass


@dataclass
class Passenger:
    id: int
    name: str
    seat_number: int
    trip_id: int

    def to_dict(self):
        return asdict(self)
