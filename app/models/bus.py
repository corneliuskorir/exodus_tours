from dataclasses import asdict, dataclass


@dataclass
class Bus:
    id: int
    driver: str
    route_id: int
    seats: int

    def to_dict(self):
        return asdict(self)


"""
{
    "id":1,
    "driver":"Mat",
    "route_id":1,
    "seats":60
}
"""
