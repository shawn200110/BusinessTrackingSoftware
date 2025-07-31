from dataclasses import dataclass

@dataclass
class Vendor:
    name: str
    part_num: str
    unit_price: float
    address: str
    city: str
    state: str
    zipcode: int
    