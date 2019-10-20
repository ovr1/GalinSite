from django.shortcuts import render
from django.views.generic.base import TemplateView

def massage(request):
    return render(request, 'massage.html')
	
	




