day_work = {9: 2619, 5: 712, 8: 1235, 10: 1440, 6: 178, 7: 1369, 4: 813, 2: 4786}
starting_day_work = day_work.copy()
work_levels = list(day_work.keys())

employees = {
'ST.E-01': {'time': 480, 1: 0, 2: 0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 0, 10: 0}, 
'ST.E-02': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}, 
'ST.E-03': {'time': 480, 1: 1.0, 2: 0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 0, 9: 0, 10: 0}, 
'ST.E-04': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 0, 10: 0}, 
'ST.E-05': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 0}, 
'ST.E-06': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}, 
'ST.E-07': {'time': 480, 1: 1.0, 2: 0, 3: 1.0, 4: 0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 0}, 
'ST.E-08': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 0}, 
'ST.E-09': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}, 
'ST.E-10': {'time': 480, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 0, 9: 0, 10: 0}, 
'ST.E-11': {'time': 480, 1: 0, 2: 0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 0, 9: 0, 10: 0}, 
'ST.E-12': {'time': 480, 1: 1.0, 2: 0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 0, 9: 0, 10: 0}, 
'ST.E-13': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 0}, 
'ST.E-14': {'time': 480, 1: 1.0, 2: 0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 0, 10: 0}, 
'ST.E-15': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-16': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 0, 9: 0, 10: 0}, 
'ST.E-17': {'time': 480, 1: 1.0, 2: 0, 3: 0, 4: 0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 0}, 
'ST.E-18': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-19': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-20': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-21': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-22': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-23': {'time': 480, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-24': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-25': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-26': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-27': {'time': 480, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-28': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-29': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-30': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-31': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-32': {'time': 480, 1: 0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-33': {'time': 480, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-34': {'time': 480, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 
'ST.E-35': {'time': 480, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
}



def calculate_employee_score(employee):

    # get all jobs that employee is able to do
    able_to_do_jobs = [list(employees[employee].keys())[1:][i] for i, x in enumerate(list(employees[employee].values())[1:]) if x == 1]
    # get all jobs that employee is able to do and are in day
    common_jobs = [w for w in able_to_do_jobs if w in day_work.keys()]

    employee_score = 0
    for job in common_jobs:
        # list of time avaiable for employees that can do specific job
        employees_time = [ x['time'] for x in employees.values() if x[job] == 1 ]

        # if work time is 0 skip to prevent divistion by 0
        if day_work[job] == 0: continue
        # add employee score for one job to overall score
        employee_score += sum(employees_time)/day_work[job]

    return employee_score



def distribut_employees_for_one_day(day_work,starting_day_work,work_levels,employees):

    for a in range(len(day_work)):
        current_work = max(work_levels)

        available_employees = {}

        # get all employees that can do work and their employee scores
        for index, employee in enumerate(employees.values()) :
            # skin employees that dont have time or cant do job
            if not employee['time'] or not employee[current_work]: continue
            employee_key = list(employees.keys())[index]
            # calculate employee score
            score = calculate_employee_score(employee_key)
            # set employee to his score
            available_employees[employee_key] = score


        for i in range(len(available_employees)):
            min_score_employee_index = list(available_employees.values()).index(min(available_employees.values()))
            employee = list(available_employees.keys())[min_score_employee_index]
            
            employee_time = employees[employee]['time']
            
            if day_work[current_work] > employee_time:
                # subtract employee time from work time
                day_work[current_work] -= employee_time
                # set employee time to 0
                employees[employee]['time'] = 0


            elif day_work[current_work] <= employee_time:
                # subtract left work time from employee time
                employees[employee]['time'] -= day_work[current_work]
                # set work time to 0
                day_work[current_work] = 0

            # delete employee from available employees
            del available_employees[employee]

        # after all delete work from day work
        work_levels.remove(current_work)

        
    print(day_work)
    print(starting_day_work)


distribut_employees_for_one_day(day_work,starting_day_work,work_levels,employees)