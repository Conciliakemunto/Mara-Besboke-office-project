import re
from django.shortcuts import render

def index(request):
    return render(request, 'mara/index.html')


def about(request):
    return render(request,'mara/about.html')

def contact(request):
    return render(request, 'mara/contact.html')
