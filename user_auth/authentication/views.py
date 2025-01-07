from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("This is about us page")

def index(request):
    return render(request,"index.html")