from django.db import models
import media

# Create your models here.
# class userpost(models.Model):
#     # name = models.CharField(max_length=30,blank=False)
#     # dp = models.ImageField(upload_to='userdp/',blank=False)
#     # description = models.TextField(max_length=400,blank=False)
#     # postimage = models.ImageField(upload_to='userpost/',blank=False)
    
#     def __str__(self):
#         return self.name
    
class mypost(models.Model):
    description = models.TextField(max_length=400)
    postimage = models.ImageField(upload_to='mypost/')
    username = models.CharField(max_length=100,default='SOME STRING' )
    def __str__(self):
        return self.description


class UserProfile(models.Model):

    first_name = models.CharField(max_length=100,default='SOME STRING')
    last_name=models.CharField(max_length=100,default='SOME STRING')
    email = models.EmailField(default='SOME STRING')
    username = models.CharField(max_length=100,default='SOME STRING' )
    password=models.CharField(max_length=100,default='SOME STRING')

    def __str__(self):
        return f"{self.username}"

class userstatus(models.Model):
    visibility = models.CharField(max_length=20,choices=[('online','online'),('offline','Offline'),('Inmeeting','Inmeeeting'),],default='online')


