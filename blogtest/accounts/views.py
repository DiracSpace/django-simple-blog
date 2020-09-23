from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

"""
# 1- if scenario is POST, than generate new user
# 2- if scenario is GET, generate a new instance
# 3- if scenario is POST but error, render a new fresh template
"""

# function for usersignup
def usersignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user registration and redirection to articles
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form':form })

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # user login and redirection to articles
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form':form })

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
