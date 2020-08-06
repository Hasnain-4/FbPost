from django.db import models

# Create your models here.

class Newsdata(models.Model):
    imagelink = models.CharField(max_length = 422,blank = True)
    heading = models.CharField(max_length = 442, blank = True)
    body = models.TextField(blank = True)
    date = models.CharField(max_length = 422,blank=True)