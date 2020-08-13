from django.shortcuts import render
from .models import Articles

# function for article list
def articles_list(request):
    listofarticles = Articles.objects.all().order_by('date')
    # returning html template render
    return render(request, 'articles/articles_list.html', { 'articles':listofarticles })
