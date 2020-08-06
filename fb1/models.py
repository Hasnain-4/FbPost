from django.db import models
from datetime import datetime , date
from django.utils.timezone import now
from django.contrib.auth.models import User , auth



# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length = 222)
    mobile_no = models.CharField(max_length = 222)
    message = models.TextField()

    def __str__(self):
        
        return self.name

class Imagepost(models.Model):

    imagename = models.ImageField()
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    image = models.ImageField()

class Videopost(models.Model):

    videoname = models.ImageField()
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    utube_video_link = models.CharField(max_length = 2222)
    
class Userprofile(models.Model):
    profilepic = models.ImageField(default = 'static/images/hasntravel.jpg')
    about = models.TextField()

class Postcomment(models.Model):
    message1 = models.CharField(max_length = 222)
    date = models.DateTimeField(default=datetime.now())

    


    
    
