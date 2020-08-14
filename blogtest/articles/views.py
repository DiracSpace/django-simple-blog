from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# function for article list
def articles_list(request):
    listofarticles = Articles.objects.all().order_by('date')
    # returning html template render
    return render(request, 'articles/articles_list.html', { 'articles':listofarticles })

# function for url capturing
def articles_detail(request, slug):
    # search db for article route
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', { 'article':article })
