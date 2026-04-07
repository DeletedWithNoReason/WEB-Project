from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserLoginForm 

def homepage(request):
    return render(request, 'users/homepage.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, phone=identifier, password=password) 
            
            if user is not None:
                login(request, user)
                return redirect('users:homepage')
            else:
                messages.error(request, "Invalid phone or password.")
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('users:homepage')
    
  
    return render(request, 'users/logout_confirm.html')