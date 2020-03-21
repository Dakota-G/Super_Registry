from django.db import models

class User(models.Model):  
    alias = models.CharField(max_length = 25)
    name = models.CharField(max_length = 50)
    alignment = models.CharField(choices=['hero', 'villain'])
    weakness = models.CharField()
    nemeses = models.ManyToManyField("self")
    description = models.TextField(max_length=250)

class Powers(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length=250)
    users = models.ManyToManyField("User", related_name="powers")