
levels = [1,2,3,4]


employees = {
    'id_1': [1,2],
    'id_2': [1,3],
    'id_3': [1,4],
    'id_4': [2,3],
    'id_5': [2,4],
    'id_6': [3,4],
}

emp_score = {
    'id_1': 0,
    'id_2': 0,
    'id_3': 0,
    'id_4': 0,
    'id_5': 0,
    'id_6': 0,
}


for emp in employees.keys():
    emp_score[emp] = len(list(set(levels).intersection(employees[emp])))


print(min(emp_score, key=emp_score.get))

if not 'id' in emp_score.keys():
    print('hi')




employees_hours = {
    'id_1': 8,
    'id_2': 8,
    'id_3': 8,
    'id_4': 8,
    'id_5': 8,
    'id_6': 8,
}



work = {
    '1':12, 
    '2':14, 
    '3':9, 
    '4':13, 
}

e_by_work = {
    '1':[],
    '2':[],
    '3':[],
    '4':[],
}

for employee in employees.keys():
    skills = employees[employee]
    for value in work.keys():
        if int(value) in skills:
            e_by_work[value].append(employee)





work_time = 48
emps_time = 48


ratio = []
#calculate work time and workers time ration
for key in work.keys():
    ratio.append(work[key]/(len(e_by_work[key]) * 8)) 


leng = len(ratio)
i = 0

while True:

    i+=1

    print('ITERATION  :   ' + str(i))


    for emp in employees.keys():
        emp_score[emp] = len(list(set(levels).intersection(employees[emp])))
    print(emp_score.values())
    
    job = len(ratio)
    job_time = work[str(job)]
    
    print(job)
    for f in range(len(employees)):

        employee = min(emp_score, key=emp_score.get)
        print(employee)
        
        if not employee in e_by_work[str(job)]:
            del emp_score[employee]
            continue

        emp_time = employees_hours[employee]
        
        if emp_time > 0 and job_time > emp_time:
            s_time = emp_time
            job_time -= emp_time
            work[str(job)] -= emp_time
            work_time -= emp_time
            emps_time -= emp_time
            emp_time = 0
            employees_hours[employee] = 0
            del emp_score[employee]
            # print(employee + ' : ' + str(s_time - emp_time))
            # print(job_time,work[str(job)],work_time)

        elif emp_time > 0 and job_time < emp_time:
            s_time = emp_time
            emp_time -= job_time
            employees_hours[employee] -= job_time
            work_time -= job_time
            emps_time -= job_time
            job_time = 0
            work[str(job)] = 0
            del emp_score[employee]
            # print(employee + ' : ' + str(s_time - emp_time))
            # print(job_time,work[str(job)],work_time)
        else:
            del emp_score[employee]
            

    levels.remove(len(ratio))
    ratio.remove(ratio[-1])
    
    if i == leng:
        break


print(work)
print(employees_hours)

