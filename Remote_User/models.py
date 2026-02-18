from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,  default='Unknown')
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10,  default='Unknown')
    country = models.CharField(max_length=30,  default='Unknown')
    state = models.CharField(max_length=30,  default='Unknown')
    city = models.CharField(max_length=30, default='Unknown')
    gender= models.CharField(max_length=30, default='Unknown')
    # address= models.CharField(max_length=30)
    address = models.CharField(max_length=255, default='Unknown')


class predict_poisoning_attack(models.Model):

    title= models.CharField(max_length=30000)
    pubDate= models.CharField(max_length=30000)
    guid= models.CharField(max_length=30000)
    link= models.CharField(max_length=30000)
    desc1= models.CharField(max_length=30000)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



