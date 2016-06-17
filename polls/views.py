from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#this is the simplest view possible in Django. To call the view, we map it to a URL. We make a URLconf in urls.py
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
