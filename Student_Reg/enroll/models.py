from django.db import models

# Create your models here.
class City(models.Model):
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.city

class Skill(models.Model):
    skills=models.CharField(max_length=20)
    def __str__(self):
        return self.skills

class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    skill=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    def __str__(self):
        return self.name
  