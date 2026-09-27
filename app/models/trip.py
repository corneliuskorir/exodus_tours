from dataclasses import asdict, dataclass

from .bus import Bus
from .passenger import Passenger
from .route import Route


@dataclass
class Trip:
    id: int
    bus: Bus
    route: Route
    available_seats: int
    status: str
    passengers: list[Passenger]

    def __post_init(self):
        self.available_seats = self.bus.seats
        if self.status not in ("pending", "complete", "in_progress"):
            raise ValueError("status must be pending, complete, in_progress")

    def to_dict(self):
        return asdict(self)
