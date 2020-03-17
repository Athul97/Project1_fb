from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)


class Sgup(models.Model):
    firstname = models.CharField(max_length=25)
    surname   = models.CharField(max_length=25)
    dob       = models.DateField(default=None)
    gender    = models.CharField(max_length=10)
    login     = models.ForeignKey(Login, on_delete=models.CASCADE)


class Profilepic(models.Model):
    image = models.FileField(upload_to='profilepic/')
    login = models.ForeignKey(Login,on_delete=models.CASCADE)