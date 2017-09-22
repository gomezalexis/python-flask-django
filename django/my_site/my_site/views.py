from django.http import HttpResponse

def home_page(request):
    response = "This is the homepage."
    return HttpResponse(response)