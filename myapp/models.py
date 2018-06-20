from django.db import models
# Create your models here.

class data(models.Model):
    file = models.FileField(default=None, null=True, blank=True)
    name = models.CharField(max_length=250, null =True)
    email = models.CharField(max_length=250, null= True)
