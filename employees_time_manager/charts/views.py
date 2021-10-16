from django.shortcuts import render, redirect
from .models import Employee
from .functions.csv_filtering_work import filter_work_data
from .functions.csv_filtering_employees import filter_employees_data
from .functions.distributing import distribut_employees_for_one_day
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def get_csv(request):
    # form = getCsv()
    if request.method == 'POST':

        # if csv file is empty
        if not request.FILES.get('uploaded_file'):
            messages.error(request, 'Nie dodany pliku csv!')
            return redirect('get_csv')

        # get uploaded file content
        csv = request.FILES.get('uploaded_file').read()
        # print(csv)

        #create sessions csv file and convert it from bytes to string format
        request.session['csv'] = csv.decode("utf-8") 


        return redirect('display_charts')
 


    return render(request, 'charts/paste_csv.html')

@login_required(login_url='login')
def display_charts(request):

    csv = request.session.get('csv')

    try:
        sorted_work_data = filter_work_data(csv)
        employees = Employee.objects.all().values()



        distribution = {}
        for date in sorted_work_data:
            day = sorted_work_data[date]
            starting_day_work = day.copy()
            work_day = day.copy()
            
            employees_data = filter_employees_data(employees)
            work_levels = list(day.keys())

            distributed_day = distribut_employees_for_one_day(work_day,starting_day_work,work_levels,employees_data)
            distribution[date] = distributed_day

    
        return render(request, 'charts/display_charts.html', {'data':distribution})
        
    except:
        messages.error(request, 'Twój plik csv jest w złej formie!')
        return redirect('get_csv')
    


@login_required(login_url='login')
def employees_table(request):

    login_user = request.user

    if request.method == 'POST':
        data = request.POST
        
        # delete all objects before updating
        Employee.objects.all().delete()

        for key in list(data.keys())[1:]:

            employee = Employee()
            employee.user = login_user
            employee.table_row = key
            
            employee_data = data.getlist(key)
            employee.employee_id = employee_data[0]
            employee.presence = employee_data[1]
            for i in range(1,11):
                skill_name = 'E' + str(i).zfill(2)
                
                setattr(employee, skill_name, employee_data[i+1])

            employee.save()

        return redirect('get_csv')

    else:
        
        data = login_user.employee_set.all()

        return render(request, 'charts/employees_table.html', {'data':data})





    