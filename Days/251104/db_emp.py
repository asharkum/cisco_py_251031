'''This module handles reading and writing employee data to a binary file using pickle.'''
import pickle
import os

FILE_NAME ='employee_db.dat'

def read_employees():
    '''Reads the list of employees from a binary file.'''
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'rb') as file:
        return pickle.load(file)

def write_employees(employee_list):
    '''Writes the list of employees to a binary file.'''
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(employee_list, file)

print(read_employees())
