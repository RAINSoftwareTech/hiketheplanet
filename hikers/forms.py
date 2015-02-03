from django import forms
from django.contrib.auth.models import User
from hikers.models import Hiker


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class HikerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ('home_zipcode',
                  'profile_pic')


