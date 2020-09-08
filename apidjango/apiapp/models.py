from django.db import models

# Create your models here.

class Form(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    adress1=models.CharField(max_length=100)
    adress2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

    def __str__(self):
        return self.fname