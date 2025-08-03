from dataclasses import dataclass

@dataclass
class Vendor:
    vendor_name: str
    part_id: str
    part_num: str
    unit_price: float
    address: str
    city: str
    state: str
    zipcode: int
    