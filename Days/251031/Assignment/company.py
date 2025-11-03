"""
Contains the Company class to manage a list of Employee objects.
"""
from employee import Employee

class Company:
    """Class representing a company that manages employees."""
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee Added successfully \n")

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def update_employee(self, emp_id, new_salary):
        emp = self.search_employee(emp_id)
        if emp:
            emp.salary = new_salary
            print("Employee updated successfully \n")
        else:
            print("Employee not found \n")  

    def delete_employee(self, emp_id):
        emp = self.search_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print("Employee delete successfully \n")
        else:
            print("Employee not found \n")

    def display_all(self):
        if not self.employees:
            print("No employee found, it’s empty \n")
        else:
            print("Employee List \n")
            for emp in self.employees:
                print(emp)
            print()