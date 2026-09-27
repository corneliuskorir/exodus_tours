from dataclasses import asdict, dataclass


@dataclass
class Bus:
    id: int
    driver: str
    route_id: int
    seats: int

    def to_dict(self):
        return asdict(self)
