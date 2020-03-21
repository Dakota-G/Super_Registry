from django.shortcuts import render

def choose(request):
    return render(request, 'index.html')

def register_power(request):
    pass