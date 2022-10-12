import re
from django.shortcuts import render

def index(request):
    return render(request, 'mara/index.html')

from django.shortcuts import render

def about(request):
    return render(request,'mara/about.html')
