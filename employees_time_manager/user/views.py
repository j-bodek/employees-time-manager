from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username = username, password = password)
            print(user)

            if user:
                login(request,user)
                messages.success(request, 'Logowanie powiodło się')
                return redirect('get_csv')
            else:
                messages.error(request, 'Login lub hasło są niepoprawne!')


        except:
            messages.error(request, 'Login nie istnieje!')


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
                NewUser.set_password(password1)
                NewUser.save()

                messages.success(request, 'Konto zostało utworzone')
                return redirect('login_user')
            else:
                # display not matching password message
                messages.error(request, 'Hasła są różne!')
        else:
            #display taken username message
            messages.error(request, 'Podany login już istnieje!')
            



    return render(request, 'user/login_register.html', {'form':'register'})



@login_required(login_url='login_user')
def logout_user(request):
    user = request.user
    print(user)
    logout(request)
    messages.error(request, f'Użytkownik {user} wylogowany!')
    return redirect('login_user')