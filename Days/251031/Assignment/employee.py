"""
employee.py
Contains the Employee class representing an employee's details.
"""
class Employee:
    """
    Class representing an employee.

    Attributes:
        id (int): Employee ID
        name (str): Employee name
        job_title (str): Employee job title
        salary (float): Employee salary
    """
    def __init__(self,emp_id,name,job_title,salary):         #dunder method
        self.id = emp_id
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def __str__(self):      #dunder method like toString -> how an object should look when you print it
         return f"ID: {self.id}, Name: {self.name}, Title: {self.job_title}, Salary: {self.salary}"

