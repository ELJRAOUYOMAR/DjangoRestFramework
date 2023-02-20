from django.db import models
from datetime import datetime
# Create your models here.

# Guest -- Movie -- Reservation
class Movie(models.Model):
    hall=models.CharField(max_length=12)
    movie=models.CharField(max_length=12)
    date=models.DateField(default=datetime.now())
    def __str__(self):
        return self.movie

class Guest(models.Model):
    name= models.CharField(max_length=12)
    mobile= models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE,related_name='reservation')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reservation')
# class JsonFormat(models.Model):
#     name= models.CharField(max_length=12)
#     last= models.CharField(max_length=12)
#     phone= models.CharField(max_length=12)
    
