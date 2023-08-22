from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class IdCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200)
    typecard = models.CharField(max_length=100)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    nationality = models.CharField(max_length=200)
    height = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    dateofbirth = models.CharField(max_length=30)
    haircolor = models.CharField(max_length=50)
    eyecolor = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    birthcertificate = models.CharField(max_length=200)
    du = models.CharField(max_length=20)
    docnumber = models.CharField(max_length=200)
    expiry = models.CharField(max_length=20)
    placeofissue = models.CharField(max_length=200)
    
    def __str__(self):
        return self.docnumber