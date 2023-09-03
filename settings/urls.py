# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.settings,name='settings'),
    path('settings-change/',views.settingspassword,name='settings-change'),
    # path('settings-user-details/',views.settingsuserdetails,name='settings-user-details'),

]