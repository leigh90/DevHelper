from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Resource(models.Model):
    programming_language = models.CharField(max_length=200)
    topic = models.CharField(max_length=300)
    link = models.URLField(max_length=128,db_index=True,unique=True,blank=True)
    resource_image = CloudinaryField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    