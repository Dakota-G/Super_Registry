from django.db import models


class User(models.Model):
    Alias = models.CharField(max_length = 25)
    Name = models.CharField(max_length = 50)
    Powers = models.CharField()