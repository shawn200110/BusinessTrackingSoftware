import json
from models.employee import Employee

class EmployeeManager:
    def __init__(self, cash_manager, data_file="employees.json"):
        self.data_file = data_file
        self.cash_manager = cash_manager
        self.employees = []
        self.load_employees()

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        self.save_employees()

    def remove_employee(self, name: str):
        self.employees = [e for e in self.employees if e.name != name]
        self.save_employees()

    def pay_employee(self, name: str, num_weeks: int):
        employee = [e for e in self.employees if e.name == name]
        employee = employee[0]
        self.cash_manager.add_transaction(description=f"Payroll - {employee.name}", 
                                         amount=-employee.salary * (num_weeks / 52))
                                        
        # You can extend this to track payroll events, taxes, etc.
        print(f"{name} has been paid.")
        # Optionally: write a log or payroll history

    def save_employees(self):
        data = [{"name": e.name, "address": e.address, "city": e.city, 
                 "state": e.state, "zipcode": e.zipcode, "num_witholdings": e.num_witholdings,
                   "salary": e.salary} for e in self.employees]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_employees(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.employees = [Employee(**entry) for entry in data]
        except FileNotFoundError:
            self.employees = []