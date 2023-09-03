from django.shortcuts import render

# Create your views here.
from . models import userinfo,forgetpass
from user.models import UserProfile
from django.contrib.auth.models import User

def settings(request):
    if request.method == 'POST':
        fname1 = request.user.first_name
        lname1 = request.user.last_name
        username1 = request.user.username
        userpronouns1 = request.POST.get('userpronouns') 
        userbio1 = request.POST.get('userbio')
        userlink1 = request.POST.get('userlink') 
        address1 = request.POST.get('address')
        ph1 = request.POST.get('ph')
        email1 = request.user.email
        userdetailsdata = userinfo(fname=fname1,lname=lname1,username=username1,userpronouns=userpronouns1,userbio=userbio1,userlink=userlink1,address=address1,ph=ph1,email=email1)
        userdetailsdata.save()     
    return render(request,'settings.html')



def settingspassword(request):
    username=request.user.username
    user1=User.objects.filter(username=username).first()
    user2=UserProfile.objects.filter(username=username).first()
    if request.method == "POST":
        fname1=request.POST.get('fname')
        lname1=request.POST.get('lname')
        email1=request.POST.get('email')
        username1=request.POST.get('username')
        updated  =  forgetpass(fname=fname1,lname=lname1,username=username1,email=email1)
        updated.save()
        user1.first_name,user1.last_name,user1.username,user1.email=fname1,lname1,username1,email1
        user1.save()
        user2.first_name,user2.last_name,user2.username,user2.email=fname1,lname1,username1,email1
        user2.save()
    return render(request,'settings-password.html')



