# from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.popuplar, name='popular'),
    path('popularstate/', views.popularstate, name='popularstate'),
    path('popularcity/', views.popularcity, name='popularcity'),
    path('popularpremium/', views.popularpremium, name='popularpremium'),
    path('popularworld/', views.popularworld, name='popularworld'),
    path('popularindia/', views.popularindia, name='popularindia'),
    path('populartechnology/', views.populartechnology, name='populartechnology'),

]
