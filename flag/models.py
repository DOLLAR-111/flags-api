from django.db import models

# Create your models here.



class Flags(models.Model):
    flag_name = models.CharField(max_length=100)
    flag_description = models.TextField()
    images = models.ImageField(upload_to="images/")
    