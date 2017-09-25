from django.http import HttpResponse

def home_page(request):
    hola = "Ola ke asen"
    return HttpResponse(hola)