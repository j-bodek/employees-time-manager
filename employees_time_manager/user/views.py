from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'user/login_register.html', {'form':'login'})

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if not user:
            if password1 == password2:
                # create new user
                print(username, password2)
                NewUser = User()
                NewUser.username = username
                NewUser.password = password1
                NewUser.save()
                return redirect('login')
            else:
                # display not matching password message
                messages.error(request, 'Hasła są różne!')
        else:
            #display taken username message
            messages.error(request, 'Podany login już istnieje!')
            



    return render(request, 'user/login_register.html', {'form':'register'})