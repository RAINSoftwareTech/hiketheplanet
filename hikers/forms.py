from django import forms

from localflavor.us.forms import USZipCodeField, USStateField
from localflavor.us.us_states import STATE_CHOICES
from timezones.zones import PRETTY_TIMEZONE_CHOICES

from hikers.models import Hiker, HikerAddress, HikerDiaryEntry, HikerPhoto


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


class HikerBasicInfoForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Hiker
        fields = ('first_name', 'last_name', 'email',
                  'timezone', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(HikerBasicInfoForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            raise ValueError('{} should not be called from a CreateView.'
                             'New Hiker instances should only be created from'
                             'the registration.'.format(self))
        else:
            hiker = self.instance.hiker
            self.initial['first_name'] = hiker.first_name
            self.initial['last_name'] = hiker.last_name
            self.initial['email'] = hiker.email

    def save(self, *args, **kwargs):
        hiker = self.instance.hiker
        hiker.first_name = self.cleaned_data['first_name']
        hiker.last_name = self.cleaned_data['last_name']
        hiker.email = self.cleaned_data['email']
        hiker.save()
        return super(HikerBasicInfoForm, self).save(*args, **kwargs)


class HikerStatsForm(forms.ModelForm):

    class Meta:
        model = Hiker
        fields = ('health_level', 'avg_walking_pace')

    def __init__(self, *args, **kwargs):
        super(HikerStatsForm, self).__init__(*args, **kwargs)
        self.fields['avg_walking_pace'].localize = True


class HikerAddressForm(forms.ModelForm):

    class Meta:
        model = HikerAddress
        fields = ('address_line1', 'address_line2',
                  'city', 'state', 'zipcode', 'cell_number')


class HikerDiaryForm(forms.ModelForm):

    class Meta:
        model = HikerDiaryEntry
        fields = ('title', 'diary_entry', 'hike', 'make_public')


class HikerPhotoForm(forms.ModelForm):

    class Meta:
        model = HikerPhoto
        fields = ('title', 'photo', 'hike', 'diary_entry', 'make_public')

    def __init__(self, *args, **kwargs):
        super(HikerPhotoForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = True
