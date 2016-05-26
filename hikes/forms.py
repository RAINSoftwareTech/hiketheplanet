from django import forms
from hikes.models import Hike, Trailhead, Region


class HikeForm(forms.ModelForm):

    class Meta:
        model = Hike
        fields = ('name', 'hike_type', 'difficulty_level',
                  'difficulty_level_explanation', 'distance', 'elevation',
                  'high_point', 'description', 'trail_map')

    def __init__(self, *args, **kwargs):
        super(HikeForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Hike Name'


class TrailheadForm(forms.ModelForm):

    new_region = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Trailhead
        fields = ('region', 'new_region', 'name', 'latitude', 'longitude')

    def __init__(self, *args, **kwargs):
        super(TrailheadForm, self).__init__(*args, **kwargs)
        self.fields['region'].required = False
        self.fields['region'].label = 'Select Region'
        self.fields['new_region'].label = 'or Enter New Region Name'
        self.fields['name'].label = 'Trailhead Name'

    def clean(self):
        region = self.cleaned_data.get('region')
        new_region = self.cleaned_data.get('new_region')
        if not region and not new_region:
            # neither was specified so raise an error to user
            raise forms.ValidationError('Must specify either '
                                        'region or New region!')
        elif not region:
            region, created = Region.objects.get_or_create(name=new_region)
            self.cleaned_data['region'] = region

        return super(TrailheadForm, self).clean()

HikeFormset = forms.inlineformset_factory(
    Trailhead, Hike,
    form=HikeForm,
    extra=1, can_delete=False)
