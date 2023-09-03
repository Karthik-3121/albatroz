from django.contrib import admin

# Register your models here.
from .models import mypost,UserProfile,userstatus
# admin.site.register(userpost)
admin.site.register(mypost)
admin.site.register(UserProfile)
admin.site.register(userstatus)
