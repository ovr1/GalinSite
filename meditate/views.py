from django.shortcuts import render
from django.views.generic.base import TemplateView

def meditate(request):
    return render(request, 'meditate.html')
