from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField('name',max_length=100)
    contact = models.CharField('contact',max_length=10)