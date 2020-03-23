from django.db import models
import datetime, time

class UserManager(models.Manager):
    # Creates a validator for the User class below
    def User_Val(self, POSTdata):
        errors = {}
        if len(POSTdata['alias']) == 0:
            errors['alias'] = "Please enter an alias!"
        if len(POSTdata['name']) == 0:
            errors['name'] = "Please enter a real name!"
        if len(POSTdata['name']) < 3:
            errors['name'] = "Please enter a longer name!"
        if not POSTdata['name'].isalpha():
            errors['name'] = "Please only enter letters for the name!"
        if len(POSTdata['weakness']) == 0:
            errors['weakness'] == "Please add at least one weakness!"
        if len(POSTdata['description']) == 0:
            errors['description'] = "Please add a description!"
        elif len(POSTdata['description']) < 2:
            errors['description'] = "Please add a longer description!"
        return errors
        
class PowerManager(models.Manager):
    def Power_Val(self, POSTdata):
        errors = {}
        if len(POSTdata["name"]) == 0:
            errors["name"] = "Please name the power!"
# This will check to see if the power name is unique by searching the database
        related = Powers.objects.filter(name = POSTdata["name"])
        if len(related) > 0:
            errors["name"] = "The power's name is not unique! Check the database!"
        if len(POSTdata["description"]) < 10:
            errors["description"] = "Please describe the power with some detail!"
        return errors

class TeamManager(models.Manager):
    def Team_Val(self, POSTdata):
        errors = {}
        warnings = {}
        today = str(datetime.date.today())
        if len(POSTdata['name']) == 0:
            errors['name'] = "Please enter a team name!"
        related_active = Team.objects.filter(name = POSTdata['name'], active = True)
        if len(related_active) > 0:
            errors['name'] = "Your team's name clashes with a currently active team!"
        related_inactive = Team.objects.filter(name = POSTdata['name'], active = False)
        if len(related_inactive) > 0:
            warnings['name'] = "Be aware: Your team's name reuses a currently inactive team name!"
        if time.strptime(POSTdata['inception'], "%Y-%m-%D") > time.strptime(today, "%Y-%m-%D"):
            warnings['inception'] = "Be aware: Your inception date is in the future!"
        messages = [errors, warnings]
        return messages        

class User(models.Model):  
    alias = models.CharField(max_length = 25)
    name = models.CharField(max_length = 50)
    alignment = models.CharField(max_length = 1, choices=[('h','hero'), ('v','villain')])
    weakness = models.CharField(max_length = 25)
    nemeses = models.ManyToManyField("self")
    description = models.TextField(max_length = 250)
    objects = UserManager()

class Powers(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length = 250)
    users = models.ManyToManyField("User", related_name="powers")
    objects = PowerManager()

class Team(models.Model):
    name = models.CharField(max_length = 50)
    headquarters = models.CharField(max_length = 100)
    inception = models.DateField()
    active = models.BooleanField(default = True)
    description = models.TextField(max_length = 250)
    leader = models.ForeignKey("User", related_name="team_lead", on_delete=models.CASCADE)
    members = models.ManyToManyField("User", related_name="team")
    objects = TeamManager()