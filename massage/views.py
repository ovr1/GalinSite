from django.shortcuts import render

def massage(request):
    return render(request, 'massage.html')

def static(request):
    return render(static)