from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar


@dataclass
class Employee(ABC):
    name: str
    emp_id: str = None
    _company: Company = None
    _last_assigned_id: ClassVar[int] = 0

    def __post_init__(self):
        self.emp_id = "E" + str(Employee._last_assigned_id)
        Employee._last_assigned_id += 1

    @abstractmethod
    def calculate_payment(self):
        pass

    def leave_company(self):
        if self._company is None:
            print(f"Employee is not currently employed by any company")
        else:
            self._company.fire(self)

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company: Company):
        self._company = company

class HourlyEmployee(Employee):
    def __init__(self, name: str, rate: int):
        self._hourly_rate = rate
        super().__init__(name)

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate: int):
        self._hourly_rate = rate

    def calculate_payment(self):
        return self._hourly_rate * 40


class SalariedEmployee(Employee):
    def __init__(self, name: str, salary: int):
        self._salary = salary
        super().__init__(name)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: int):
        self._salary = salary

    def calculate_payment(self):
        return self._salary / 4

class Domain(Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    RETAIL = "Retail"

@dataclass
class Company:
    name: str
    domain: Domain
    employees: list[Employee] = field(default_factory=list)


    def hire(self, employee: Employee):
        if not self.is_hired_employee(employee):
            if not employee.company:
                self.employees.append(employee)
                employee.company = self
            else:
                print(f"Employee {employee.name} is hired by another company")
        else:
            print(f"Employee {employee.name} is already hired and works in this company")


    def fire(self, employee: Employee):
        if self.is_hired_employee(employee):
            self.employees.remove(employee)
            employee.company = None
        else:
            print(f"Employee {employee.name} doesn't exist")


    def raise_pay(self, employee: Employee, amount: int):
        if self.is_hired_employee(employee):
            if isinstance(employee, HourlyEmployee):
                employee.hourly_rate += amount
            else:
                employee.salary += amount

    def __repr__(self):
        return f"Company({self.name}, {self.domain.name}, Employees: {len(self.employees)})"

    def is_hired_employee(self, employee: Employee):
        return employee in self.employees

