from django.db import models

# Create your models here.

class User(models.Model) :

    uname = models.CharField(max_length=10)
    pwrd = models.CharField(max_length=10)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)

