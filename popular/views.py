from django.shortcuts import render
from django.http import HttpResponse
from . models import popularnewsall

# Create your views here.
def popuplar(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popular.html',context)

def popularstate(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popularstate.html',context)

def popularcity(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popularcity.html',context)

def popularpremium(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popularpremium.html',context)

def popularworld(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popularworld.html',context)

def popularindia(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'popularindia.html',context)

def populartechnology(request):
    populardetails = popularnewsall.objects.all()
    context={
        'popularnewsall':populardetails
    }
       
    return render(request,'populartechnology.html',context)

