from django.db import models

#Create your models here.
class cardata(models.Model):
    madelname = models.CharField('Model name',max_length=100)
    makeyear = models.CharField('Make year',max_length=4)