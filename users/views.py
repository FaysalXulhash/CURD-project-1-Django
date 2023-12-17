from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data['username']
            messages.success(request,f'{ un } s profile created successfully!!!')
            return redirect('user-register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register_user.html', {'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('student-list')
        else:
            form = AuthenticationForm()     
    else:
        return redirect('student-list')
    return render(request, 'users/user_login.html', {'form':form} )

def user_logout(request):
    logout(request)
    return redirect('user-login')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', {'name':request.user})
    else:
        return redirect('user-login')