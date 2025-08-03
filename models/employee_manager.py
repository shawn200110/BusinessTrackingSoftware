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

        payroll_info = self.calculate_payroll_taxes(employee, num_weeks)

        self.cash_manager.add_transaction(description=f"Payroll - {employee.name}", 
                                         amount=-employee.salary * (num_weeks / 52),
                                         transaction_type="payroll",
                                         payroll_info=payroll_info)
        print(f"{name} has been paid.")

    def save_employees(self):
        data = [{"name": e.name, "address": e.address, "city": e.city, 
                 "state": e.state, "zipcode": e.zipcode, "num_witholdings": e.num_witholdings,
                   "salary": e.salary, "num_dependents": e.num_dependents,
                   "filing_status": e.filing_status} for e in self.employees]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_employees(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.employees = [Employee(**entry) for entry in data]
        except FileNotFoundError:
            self.employees = []

    def calculate_payroll_taxes(self,employee, num_weeks):
        gross = employee.salary * (num_weeks / 52)

        FEDERAL_TAX_BASE_RATE = 0.19
        STATE_TAX = 0.05
        SOCIAL_SECURITY_RATE = 0.062
        MEDICARE_RATE = 0.0145

        if employee.filing_status == "married":
            federal_rate = FEDERAL_TAX_BASE_RATE - 0.02  # slight tax break
        elif employee.filing_status == "head_of_household":
            federal_rate = FEDERAL_TAX_BASE_RATE - 0.01
        else:
            federal_rate = FEDERAL_TAX_BASE_RATE

        dependent_credit = employee.num_dependents * 150  # flat $150 per dependent
        federal_tax = max(0, gross * federal_rate - dependent_credit)

        state_tax = gross * STATE_TAX
        social_security_tax = gross * SOCIAL_SECURITY_RATE
        medicare_tax = gross * MEDICARE_RATE

        total_tax = federal_tax + state_tax + social_security_tax + medicare_tax
        net = gross - total_tax

        return {
            "salary": round(gross, 2),
            "federal_tax": round(federal_tax, 2),
            "state_tax": round(state_tax, 2),
            "social_security_tax": round(social_security_tax, 2),
            "medicare_tax": round(medicare_tax, 2),
            "amount_paid": round(net, 2)
        }