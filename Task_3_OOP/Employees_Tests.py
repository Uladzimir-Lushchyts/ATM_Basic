from Employees import *

def test_data_prep():
    #Initializing 2 different companies
    company_1 = Company("Hospital", Domain.HEALTHCARE)
    company_2 = Company("Shop", Domain.RETAIL)

    ##Initializing employees of different types
    employee_1 = HourlyEmployee("Vasily",  100)
    employee_2 = SalariedEmployee("Petr", 200)
    employee_3 = HourlyEmployee("Gena",  120)
    employee_4 = SalariedEmployee("Jacob", 250)

    #Hiring employees
    company_1.hire(employee_1)
    company_1.hire(employee_2)
    company_2.hire(employee_3)
    company_2.hire(employee_4)

    return company_1, company_2, employee_1, employee_2, employee_3, employee_4


def hire_test():
    #Initializing companies and employees
    c1, c2, e1, e2, e3, e4 = test_data_prep()

    # Company 1 has hired employee 1 and 2
    assert c1.employees == [e1, e2]

    # Company 2 has 2 employees as well
    assert len(c2.employees) == 2

    # emp_id is unique for each employee
    assert e1.emp_id not in (e2.emp_id, e3.emp_id, e4.emp_id)

    #Already hired employee not duplicated
    c1.hire(e1)
    assert c1.employees == [e1, e2]

def fire_test():
    # Initializing companies and employees
    c1, c2, e1, e2, e3, e4 = test_data_prep()

    #Firing employee 1 employee
    c1.fire(e1)
    assert c1.employees == [e2]
    assert e1.company is None

    #Firing the last employee in company 1
    c1.fire(e2)
    assert c1.employees == []

    #Firing not hired employee
    c1.fire(e3)
    assert c1.employees == []
    assert c2.employees == [e3, e4]
    assert e3.company == c2

def rate_and_salary_test():
    # Initializing companies and employees
    c1, c2, e1, e2, e3, e4 = test_data_prep()

    #Setting rate for employee 1
    e1.hourly_rate = 110
    assert e1.hourly_rate == 110

    #Setting salary for employee 2
    e2.salary = 210
    assert e2.salary == 210

    #Calculating payment for employee 1
    assert e1.calculate_payment() == 110 * 40

    # Calculating payment for employee 2
    assert e2.calculate_payment() == 210 / 4

    #Raising payment for hourly employee 3
    c2.raise_pay(e3, 10)
    assert e3.hourly_rate == 130

    # Lowering payment for salaried employee 4
    c2.raise_pay(e4, -1)
    assert e4.salary == 249

def leave_company_test():
    # Initializing companies and employees
    c1, c2, e1, e2, e3, e4 = test_data_prep()

    # Employee 1 leaving the company
    e1.leave_company()
    assert e1.company is None
    assert c1.employees == [e2]

def repr_test():
    # Initializing companies and employees
    c1, c2, e1, e2, e3, e4 = test_data_prep()

    assert c1.__repr__() == "Company(Hospital, HEALTHCARE, Employees: 2)"
    assert c2.__repr__() == "Company(Shop, RETAIL, Employees: 2)"

if __name__ == "__main__":
    hire_test()
    fire_test()
    rate_and_salary_test()
    leave_company_test()
    repr_test()