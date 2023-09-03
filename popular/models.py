from django.db import models

# Create your models here.

class popularnewsall(models.Model):
    newstitle = models.CharField(max_length=40,blank=False)
    newstitlematch = models.CharField(max_length=40,blank=False)
    newsheading = models.TextField(max_length=250,blank=False)
    newslink = models.TextField(max_length=250,blank=False)

    
    