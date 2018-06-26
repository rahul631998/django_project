from django.db import models
# Create your models here.

class data(models.Model):
    upload_your_image = models.ImageField(default=None, null=True)
    min_range = models.PositiveIntegerField(max_length=5, null =True)
    max_range = models.PositiveIntegerField(max_length=5, null= True)



