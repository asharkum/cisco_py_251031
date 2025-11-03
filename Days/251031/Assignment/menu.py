"""
This module runs the Employee Management System (EMS) interactive menu.
"""
from employee import Employee
from company import Company

def main():
    """Run the EMS menu allowing add, search, update, delete, and display employees."""
    company = Company()

    while True:
        print("==========Employee Management============")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Display All Employees")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                emp_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                title = input("Enter job title: ")
                salary = float(input("Enter Salary: "))
                emp = Employee(emp_id, name, title, salary)
                company.add_employee(emp)

            case 2:
                emp_id = int(input("Enter employee id to search: "))
                emp = company.search_employee(emp_id)
                if emp:
                    print("Employee found \n")
                    print(emp, "\n")
                else:
                    print("Employee not found \n")

            case 3:
                emp_id = int(input("Enter employee id: "))
                salary = float(input("Enter new salary to update: "))
                company.update_employee(emp_id, salary)

            case 4:
                emp_id = int(input("Enter emp_id to delete: "))
                company.delete_employee(emp_id)

            case 5:
                company.display_all()

            case 6:
                print("Thank You for using Employee Management System")
                break

            case _:
                print("Invalid Choice. Please select between 1 to 6")


if __name__ == "__main__":
    main()