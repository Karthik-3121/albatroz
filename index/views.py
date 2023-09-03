from django.shortcuts import render,redirect
from user.models import mypost
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    
    if request.user.is_authenticated:
        id=request.user.username
        users = list(mypost.objects.all().order_by('-id'))
        user_ls = []
        for user in users:
            if user.username != id:
                user_ls.append(user)
        context = {
            'mypost': user_ls
        } 
        return render(request,'index.html',context)
    else:
        return redirect('logout')