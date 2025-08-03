from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    address: str
    city: str
    state: str
    zipcode: str
    num_witholdings: float
    salary: float
    num_dependents: int
    filing_status: str
    