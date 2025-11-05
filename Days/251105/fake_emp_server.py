from flask import Flask, request, jsonify

application = Flask(__name__) # app obj created
employees = [
    {'id': 1, 'name': 'Dravid', 'position': 'Old Coach'},
    {'id': 2, 'name': 'Sachin', 'position': 'Old God'}
]  # In-memory storage for employee records


@application.route('/employees', methods=['GET'])
def read_all_employee():
    return jsonify(employees)

@application.route('/employees/<emp_id>', methods=['GET'])
def read_employee(emp_id):
    result = None
    emp_id = int(emp_id)
    for emp in employees:
        if emp['id'] == emp_id:
            return jsonify(emp)
    return jsonify({'message': 'Employee not found'}), 404

@application.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.json
    employees.append(new_employee)
    return jsonify(new_employee), 201

@application.route('/employees/<emp_id>', methods=['PUT'])
def update_employee(emp_id):
    emp_id = int(emp_id)
    for emp in employees:
        if emp['id'] == emp_id:
            updated_data = request.json
            emp.update(updated_data)
            return jsonify(emp)
    return jsonify({'message': 'Employee not found'}), 404

@application.route('/employees/<emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    emp_id = int(emp_id)
    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'message': 'Employee not found'}), 404

application.run(debug=True, port="3000")  # Run the Flask application

''''
from flask import Flask, request, jsonify 

application = Flask(__name__)

employees = [
    {'id' : 101, 'name' : 'Abhishek'},
    {'id' : 102, 'name' : 'Dravid'}
]

@application.route('/employees', methods = ['GET'])
def read_all_employee():
    return jsonify(employees)

@application.route('/employees/<emp_id>', methods = ['GET'])
def read_employee_by_id(emp_id):
    emp_id = int(emp_id)
    queried_employee = None #
    for employee in employees:
        if employee['id'] == emp_id:
            queried_employee = employee
            break
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #
    return jsonify(queried_employee)

@application.route('/employees', methods = ['POST'])
def create_employee():
    form_employee = request.json
    employees.append(form_employee)
    return jsonify(form_employee), 201

@application.route('/employees/<emp_id>', methods = ['PUT'])
def update_employee(emp_id):
    emp_id = int(emp_id)
    queried_employee = None #
    for employee in employees:
        if employee['id'] == emp_id:
            queried_employee = employee
            break
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #
    
    form_employee = request.json
    queried_employee['name'] = form_employee['name']
    return jsonify(queried_employee)

@application.route('/employees/<emp_id>', methods = ['DELETE'])
def delete_employee(emp_id):
    emp_id = int(emp_id)
    queried_employee = None #
    for employee in employees:
        if employee['id'] == emp_id:
            queried_employee = employee
            break
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #    
    
    employees.remove(queried_employee)
    return jsonify({'message' : 'Employee Deleted Successfully'})

application.run(debug = True)
'''