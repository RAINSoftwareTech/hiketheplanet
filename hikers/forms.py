from django import forms
from django.contrib.auth.models import User

from localflavor.us.forms import USZipCodeField, USStateField
from localflavor.us.us_states import STATE_CHOICES

from hikers.models import Hiker, HikerAddress


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class HikerRegistrationForm(forms.Form):

    zipcode = USZipCodeField(initial='97219')
    city = forms.CharField(max_length=50, initial='Portland')
    state = USStateField(widget=forms.Select(choices=STATE_CHOICES),
                         initial='OR')

    def signup(self, request, user):
        hiker = Hiker.objects.create(hiker=user)
        HikerAddress.objects.create(hiker=hiker,
                                    zipcode=self.cleaned_data['zipcode'],
                                    city=self.cleaned_data['city'],
                                    state=self.cleaned_data['state'])
