from django.http import HttpResponse

def home_page(request):
    welcome = "Welcome to the Home Page"
    return HttpResponse(welcome)