from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from user.models import UserProfile

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password Invalid!')

    return render(request,'sign-in.html')

def logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully !')
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                profile=UserProfile(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                profile.save()
                return redirect('login')

        else:
            messages.error(request, 'Password and Confirm Password Not Matched')

    return render(request,'sign-up.html')




