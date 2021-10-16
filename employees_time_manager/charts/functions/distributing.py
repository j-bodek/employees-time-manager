

def calculate_employee_score(day_work,employees,employee):

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
            score = calculate_employee_score(day_work, employees, employee_key)
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

    for key in range(1,11):
        if key not in day_work.keys():
            day_work['E' + str(key).zfill(2)] = 0
            starting_day_work['E' + str(key).zfill(2)] = 0
        else:
            day_work['E' + str(key).zfill(2)] = day_work.pop(key)
            starting_day_work['E' + str(key).zfill(2)] = starting_day_work.pop(key)
        
    return {'day_work':day_work, 'starting_day_work':starting_day_work}


# distribut_employees_for_one_day(day_work,starting_day_work,work_levels,employees)