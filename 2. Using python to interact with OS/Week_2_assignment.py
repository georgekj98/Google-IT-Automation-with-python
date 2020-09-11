#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        new = {'Department':data['Department'], 'Username':data['Username'], 'Full Name': data['Full Name']}
        employee_list.append(new)
        
    return employee_list
 
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data={}
    for dept_name in set(department_list):
        department_data[dept_name]=department_list.count(dept_name)    
    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

emp_list = read_employees('../data/employees.csv')
dept_data =process_data(emp_list)
write_report =write_report(dept_data,'../data/report.txt')
