
from turtle import title
from django.db import models

# Create your models here.
class Todoapp(models.Model):
    title =models.CharField(max_length=1000)
    text =models.CharField(max_length=1000)
    statue=models.CharField(max_length=10)
    time=models.DateTimeField(auto_now_add=True)
