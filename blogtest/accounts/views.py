from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# function for usersignup
def usersignup(request):
    # 1- if scenario is POST, than generate new user
    # 2- if scenario is GET, generate a new instance
    # 3- if scenario is POST but error, render a new fresh template
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user login
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form':form })
