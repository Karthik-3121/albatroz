from django.contrib import admin
from import_export.admin import ImportExportMixin
# Register your models here.

from .models import popularnewsall
class popularform(ImportExportMixin,admin.ModelAdmin):
    list_display = ['newstitle','newsheading','newslink']
admin.site.register(popularnewsall,popularform)

