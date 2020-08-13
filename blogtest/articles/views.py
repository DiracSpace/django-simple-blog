from django.shortcuts import render

# function for article list
def articles_list(request):
    # returning html template render
    return render(request, 'articles/articles_list.html')
