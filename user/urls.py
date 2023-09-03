
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.profile,name='profile'),
    path('post/',views.profilepost,name='profilepost')
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




