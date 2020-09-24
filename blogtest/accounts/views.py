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
    # if request has data
    if request.method == 'POST':
        # create instance of form for new user
        form = UserCreationForm(request.POST)
        # if data in form is validated
        if form.is_valid():
            # save to db
            user = form.save()
            # login the new user
            login(request, user)
            # if unauthenticated user logins, redirect them to 
            # part of site they wanted to go 
            return redirect(request.POST.get('next')) if 'next' in request.POST else redirect('articles:list')
    else:
        # return the original empty form
        form = UserCreationForm()
    # display empty form with validation errors
    return render(request, 'accounts/signup.html', { 'form':form })

def userlogin(request):
    # if request has data
    if request.method == 'POST':
        # create instance of form for new user
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # user login and redirection to articles
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        # return the original empty form
        form = AuthenticationForm()
    # display empty form with validation errors
    return render(request, 'accounts/login.html', { 'form':form })

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
