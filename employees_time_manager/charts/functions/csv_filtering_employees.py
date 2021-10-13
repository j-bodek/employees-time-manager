import math


def filter_employees_data(data):
    sorted_employees = {}

    for employee in data:
        # continue if employee is absent
        if not employee['presence']: continue

        sorted_employees[employee['employee_id']] = {}

        # set available time for every employee (in minutes)
        sorted_employees[employee['employee_id']]['time'] = 8*60

        # loop through all work levels
        print(employee)
        for level in list(employee.keys())[5:]:
            # set work level to int
            work_level = int(level.replace('E0', '').replace('E', ''))

            # if value for work level is not specified set it to 0
            if math.isnan(employee[level]):
                sorted_employees[employee['employee_id']][work_level] = 0
            else:
                sorted_employees[employee['employee_id']][work_level] = employee[level]



    return sorted_employees