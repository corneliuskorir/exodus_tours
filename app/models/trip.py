from dataclasses import asdict, dataclass, field

from .passenger import Passenger


@dataclass
class Trip:
    id: int
    bus_id: int
    route_id: int
    status: str = "pending"
    passengers: list[Passenger] = field(default_factory=list)
    available_seats: int = 0

    def __post_init(self):
        if self.status not in ("pending", "complete", "in_progress"):
            raise ValueError("status must be pending, complete, in_progress")

    def to_dict(self):
        return asdict(self)


"""
{
    "id":1,
    "bus_id":1,
    "route_id":1
}
"""
