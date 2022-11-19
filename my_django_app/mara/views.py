import re
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mara/index.html')

def about(request):
    return render(request,'mara/about.html')

def contact(request):
    return render(request, 'mara/contact.html')

def signup(request):
    return render(request,'mara/signup.html')

def signin(request):
    return render(request,'mara/signin.html')

def signout(request):
    pass
