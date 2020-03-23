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

def view_team(request, team_id):
    try:
        team = Team.objects.get(id = team_id)
        context = {
            "team": team
        }
        return render(request, "team_viewer.html", context)
    except:
        messages.error(request, "Missing Team from Database")
        return redirect("/daemon/teams")

def all_teams(request):
    context = {
        "all_teams": Team.objects.all()
    }
    return render(request, "team_list.html", context)

# Create POST reqs
def register_power(request):
    errors = Powers.objects.Power_Val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/daemon/powers")
    else:
        new_power = Powers.objects.create(name = request.POST['name'], description = request.POST['description'])
        return redirect("/daemon/powers")

def register_user(request):
    errors = User.objects.User_Val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/daemon/user")
    else:
        new_user = User.objects.create(alias = request.POST['alias'], name = request.POST['name'], alignment = request.POST['alignment'], weakeness = request.POST['weakness'], description = request.POST['description'])
        return redirect("/daemon/user")

def register_team(request):
    m = Team.objects.Team_Val(request.POST)
    if len(m[0]) > 0:
        for key, value in m[0].items():
            messages.error(request, value, extra_tags=key)
        return redirect("/daemon/teams")
    elif len(m[1]) > 0:
        for key, value in m[1].items():
            messages.warning(request, value, extra_tags=key)
        context = {
            "warnings": m[1],
            "form": request.POST
        }
        return render(request, "verify_team.html", context)
    else:
        return register_team_finalize(request)

def register_team_finalize(request):
    if request.POST['active'] == "True":
        active = True
    else:
        active = False
    new_team = Team.objects.create(name = request.POST['name'], headquarters = request.POST['headquarters'], inception = request.POST['inception'], active = active, description = request.POST['description'])
    return redirect("/daemon/teams")

# Edit POST Reqs