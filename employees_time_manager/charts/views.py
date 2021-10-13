from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def get_csv(request):
    # form = getCsv()
    if request.method == 'POST':
        csv = request.POST.get('csv')
        print(csv)

        return redirect('display_charts')
 


    return render(request, 'charts/paste_csv.html')


def display_charts(request):
    return render(request, 'charts/display_charts.html')


def employees_table(request):

    if request.method == 'POST':
        
        data = request.POST
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


    return render(request, 'charts/employees_table.html')





    