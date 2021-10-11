import pandas as pd
import math

# open data with pandas
data = pd.read_csv('employees.csv')


sorted_employees = {}

for index, row in data.iterrows():
    # continue if employee is absent
    if not row['Obecny']: continue

    sorted_employees[row['Stanowisko']] = {}

    # set available time for every employee (in minutes)
    sorted_employees[row['Stanowisko']]['time'] = 8*60

    # loop through all work levels
    for level in row.index[2:]:
        # set work level to int
        work_level = int(level.replace('E0', '').replace('E', ''))

        # if value for work level is not specified set it to 0
        if math. isnan(row[level]):
            sorted_employees[row['Stanowisko']][work_level] = 0
        else:
            sorted_employees[row['Stanowisko']][work_level] = row[level]



print(sorted_employees)