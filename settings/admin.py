from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import userinfo,forgetpass
class userform(ImportExportMixin,admin.ModelAdmin):
    list_display = ['address','ph','userpronouns','userbio','userlink']

class passwordform(ImportExportMixin,admin.ModelAdmin):
    list_display = ['fname','lname','username','email']

admin.site.register(userinfo,userform)

admin.site.register(forgetpass,passwordform)