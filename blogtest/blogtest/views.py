from django.http import HttpResponse

# function for about url
def about(request):
    # return http HttpResponse
    return HttpResponse("about")

# function for home url
def home(request):
    # return http HttpResponse
    return HttpResponse("home")
