from django.shortcuts import render

"""
Functions for managing user ui and urls
"""

# function for about url
def about(request):
    # returning html template render
    return render(request, 'about.html')

# function for home url
def home(request):
    # returning html template render
    return render(request, 'home.html')
