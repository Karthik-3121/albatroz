from django import forms
from .models import mypost,userstatus

class mypostForm(forms.ModelForm):
    class Meta:
        model=mypost
        fields=("description","postimage")

class userstatusform(forms.ModelForm):
    class Meta:
        model = userstatus
        fields = ['visibility']