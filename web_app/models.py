from django.db import models
from cloudinary.models import CloudinaryField

class contectus(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=222)
    subject = models.TextField()

class profile(models.Model):
    image = CloudinaryField('image')
    user = models.CharField(max_length=222)




class aaddimage(models.Model):
    title = models.CharField(max_length=222)
    image = CloudinaryField('image')
    desc = models.TextField()


class maddimage(models.Model):
    title = models.CharField(max_length=222)
    image = CloudinaryField('image')
    desc = models.TextField()

class laddimage(models.Model):
    title = models.CharField(max_length=222)
    image = CloudinaryField('image')
    desc = models.TextField()
    
# Create your models here.
