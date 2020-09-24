from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Articles
from . import forms

@login_required(login_url="/accounts/login/")
# function for article list
def articles_list(request):
    # search db for all articles ordered by date
    listofarticles = Articles.objects.all().order_by('date')
    # return the render and send the object data
    return render(request, 'articles/articles_list.html', { 'articles':listofarticles })

@login_required(login_url="/accounts/login/")
# function for url capturing
def articles_detail(request, slug):
    # search db for article route
    article = Articles.objects.get(slug=slug)
    # return the render and send the object data
    return render(request, 'articles/article_details.html', { 'article':article })

@login_required(login_url="/accounts/login/")
# function for capturing article data
def create_article(request):
    # if request has data
    if request.method == 'POST':
        # create instance of form for articles
        form = forms.createArticle(request.POST, request.FILES)
        # if data in form is validated
        if form.is_valid():
            # get instance of action for saving to db
            # because we need to attach the authenticated logged in
            # user
            instanceOfArticle = form.save(commit=False)
            # we get the user that made the request for 
            # creating a new user, to attach the author
            # of an article
            instanceOfArticle.author = request.user
            # now we save to db
            instanceOfArticle.save()
            return redirect('articles:list')
    else:
        # return the original empty form
        form = forms.createArticle()
    # display empty form with validation errors
    return render(request, 'articles/article_create.html', { 'form':form })