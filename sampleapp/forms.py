from django import forms
from .models import Registration,Registrationfile

class Djangoform(forms.Form):
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    age=forms.IntegerField()
    place=forms.CharField(max_length=30)

class Registrationform(forms.ModelForm):
    class Meta:
        model=Registration
        fields="__all__" 
        # name,age,email
        # fields=["name","age"]  name age
        # exclude=['email'] name age

class Fileregistration(forms.ModelForm):
    class Meta:
        model=Registrationfile
        fields='__all__'