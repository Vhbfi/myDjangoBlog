from django.shortcuts import render
from django.shortcuts import HttpResponse


def about (request):
    # return HttpResponse('hi there! im |* vahab *| Hello World ')
    return render(request, "about.html")

def sum(request):
    return HttpResponse( 10+12 )
    

def home(request):
    # return HttpResponse("home!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request, "Home.html")