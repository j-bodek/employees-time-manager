from django.shortcuts import render, redirect
from .models import Employee
from .functions.csv_filtering_work import filter_work_data
from .functions.csv_filtering_employees import filter_employees_data

# Create your views here.
def get_csv(request):
    # form = getCsv()
    if request.method == 'POST':
        csv = request.POST.get('csv')

        #create sessions csv file
        request.session['csv'] = csv

        return redirect('display_charts')
 


    return render(request, 'charts/paste_csv.html')


def display_charts(request):

    csv = request.session.get('csv')
    sorted_work_data = filter_work_data(csv)
    employees = Employee.objects.all().values()
    employees_data = filter_employees_data(employees)
    
    
    
    return render(request, 'charts/display_charts.html')
    


def employees_table(request):

    if request.method == 'POST':
        data = request.POST
        
        # delete all objects before updating
        Employee.objects.all().delete()

        for key in list(data.keys())[1:]:

            employee = Employee()
            # employee.user_id = 120
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
            
        data = Employee.objects.all()

        return render(request, 'charts/employees_table.html', {'data':data})





    