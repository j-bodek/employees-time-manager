import pandas as pd

# open data with pandas
data = pd.read_csv('prace.csv')

sorted_data = {}

i = 0
for index, row in data.iterrows():
    # check if termin zakonczenia has hour 
    if not ' ' in row['Termin zakończenia']: continue

    # if not exist create new data in sorted data dictionary
    if not row['Data (Data rozpoczęcia)'] in sorted_data : sorted_data[row['Data (Data rozpoczęcia)']] = {}

    # convert hours to minutes
    work_time = int(row['Norma rbh do wykonania [h]'].split(':')[0]) * 60 + int( row['Norma rbh do wykonania [h]'].split(':')[1])

    # set work time 
    if row['Wartość'] in sorted_data[row['Data (Data rozpoczęcia)']]:
        # if wartosc exist in data add value to existig
        sorted_data[row['Data (Data rozpoczęcia)']][row['Wartość']] += work_time
    else: 
        # otherwise create new wartosc and set their value
        sorted_data[row['Data (Data rozpoczęcia)']][row['Wartość']] = work_time


    
    
