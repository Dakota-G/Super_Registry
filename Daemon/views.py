from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# renders
def choose(request):
    return render(request, 'index.html')

def view_power(request, power_id):
    try:
        power = Powers.objects.get(id = power_id)
        context = {
            "power": power
        }
        return render(request, "power_viewer.html", context)
    except:
        messages.error(request, "Missing Power from Database")
        return redirect("/daemon/powers")

def all_powers(request):
    context = {
        "all_powers": Powers.objects.all()
    }
    return render(request, "power_list.html", context)

# Posts
def register_power(request):
    errors = Powers.objects.Power_Val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/daemon/powers")
    else:
        new_power = Powers.objects.create(name = request.POST['name'], description = request.POST['description'])
        return redirect("/daemon/powers")