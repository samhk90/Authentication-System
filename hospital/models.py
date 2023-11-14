from django.db import models

# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
