from django.db import models



class ToDo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
