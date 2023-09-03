from django.shortcuts import render,redirect
from .models import mypost,UserProfile
from settings.models import userinfo



def profile(request):
    #frontend to backend
    if request.method == 'POST' and request.FILES['postimage']:
        # name=request.POST.get('name')
        username=request.user.username
        description=request.POST.get('description')
        postimage=request.FILES.get('postimage')
        mypostdata=mypost(description=description,postimage=postimage,username=username)
        mypostdata.save()
        redirect('profilepost')
    #backend to frontend
    username=request.user.username
    user_info=userinfo.objects.get(username=username)
    context={
        'userinfo':user_info,
    }
    return render(request,'profile.html',context)

def profilepost(request):
    id=request.user.username
    users = list(mypost.objects.all().order_by('-id'))
    user_ls = []
    for user in users:
        if user.username == id:
            user_ls.append(user)
    user_info=userinfo.objects.get(username=id)
    context={
        'mypost':user_ls,
        'userinfo':user_info,
    }
    return render(request,'profilepost.html',context)
    