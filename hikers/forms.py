from django import forms

from localflavor.us.forms import USZipCodeField, USStateField
from localflavor.us.us_states import STATE_CHOICES
from timezones.zones import PRETTY_TIMEZONE_CHOICES

from hikers.models import Hiker, HikerAddress


class HikerRegistrationForm(forms.Form):

    timezone = forms.CharField(
        widget=forms.Select(choices=PRETTY_TIMEZONE_CHOICES),
        initial='America/Los_Angeles')
    zipcode = USZipCodeField(initial='97219')
    city = forms.CharField(max_length=50, initial='Portland')
    state = USStateField(widget=forms.Select(choices=STATE_CHOICES),
                         initial='OR')

    def signup(self, request, user):
        hiker = Hiker.objects.create(hiker=user,
                                     timezone=self.cleaned_data['timezone'])
        HikerAddress.objects.create(hiker=hiker,
                                    zipcode=self.cleaned_data['zipcode'],
                                    city=self.cleaned_data['city'],
                                    state=self.cleaned_data['state'])
