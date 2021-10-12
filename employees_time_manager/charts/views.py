from django.shortcuts import render, redirect

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
    return render(request, 'charts/employees_table.html')