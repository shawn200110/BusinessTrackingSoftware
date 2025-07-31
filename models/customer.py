from dataclasses import dataclass

@dataclass
class Customer:
    company_name: str
    poc_name: str
    address: str
    city: str
    state: str
    zipcode: int
    