from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)