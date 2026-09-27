from dataclasses import asdict, dataclass


@dataclass
class Route:
    id: int
    destinations: tuple
    fare: int

    def to_dict(self):
        return asdict(self)
