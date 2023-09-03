from django.db import models

# Create your models here.
class userinfo(models.Model):
    fname = models.CharField(max_length=40,default='SOME STRING' )
    lname = models.CharField(max_length=40,default='SOME STRING' )
    username = models.CharField(max_length=15,default='SOME STRING' )
    userpronouns = models.CharField(max_length=20,default='SOME STRING' ) 
    userbio = models.TextField(max_length=250,default='SOME STRING' )
    userlink = models.TextField(max_length=400,default='SOME STRING' ) 
    address = models.TextField(max_length=100,default='SOME STRING' )
    ph = models.IntegerField(default=0 )
    email = models.CharField(max_length=100,default='SOME STRING' )
    def __str__(self):
        return self.username

    
class forgetpass(models.Model):
    fname = models.CharField(max_length=40,default='SOME STRING' )
    lname = models.CharField(max_length=40,default='SOME STRING' )
    email = models.CharField(max_length=100,default='SOME STRING' )
    username = models.CharField(max_length=15,default='SOME STRING' )

    def __str__(self):
        return self.username
    

    

    