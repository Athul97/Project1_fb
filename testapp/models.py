from django.db import models

# Create your models here.

class UserImage(models.Model):
    image = models.FileField(upload_to='gallery/')


    