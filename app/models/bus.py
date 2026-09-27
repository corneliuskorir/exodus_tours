from dataclasses import asdict, dataclass

from .route import Route


@dataclass
class Bus:
    id: int
    driver: str
    route: Route
    seats: int

    def to_dict(self):
        return asdict(self)
