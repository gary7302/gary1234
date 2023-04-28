from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import *
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.create_user(username=username, password=form.cleaned_data['password1'])
                user.save()
                return redirect('/login')
            except IntegrityError:
                form.add_error('username', 'This username already exists. Please choose a different one.')
    context={'form':form}
    return render(request,'store/auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/login')
        return render(request, 'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
    return redirect('/')



