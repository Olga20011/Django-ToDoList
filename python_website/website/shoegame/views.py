from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse("<h1>This is the home page of my website</h1>")
