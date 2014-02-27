from django.db import models

class User(models.Model):
    #TODO write here
    username = models.CharField(max_length=50)
