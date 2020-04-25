from django import forms
from hikes.models import Hike, Trailhead, Region, CountryRegion


class HikeForm(forms.ModelForm):

    region_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Hike
        fields = ('region_name', 'trailhead', 'name', 'hike_type',
                  'difficulty_level', 'difficulty_level_explanation',
                  'distance', 'elevation', 'high_point', 'description',
                  'trail_map')

    def __init__(self, *args, **kwargs):
        super(HikeForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Hike Name'
        self.fields['region_name'].widget = forms.HiddenInput()


class TrailheadForm(forms.ModelForm):

    new_region = forms.CharField(max_length=50, required=False,
                                 label='Region Name')
    co_region = forms.CharField(widget=forms.HiddenInput(), max_length=50,
                                required=False)

    class Meta:
        model = Trailhead
        fields = ('region', 'new_region', 'name', 'latitude', 'longitude')

    def __init__(self, *args, **kwargs):
        super(TrailheadForm, self).__init__(*args, **kwargs)
        self.fields['region'].label = 'Region Name'
        self.fields['name'].label = 'Trailhead Name'

    def clean(self):
        region = self.cleaned_data.get('region')
        new_region = self.cleaned_data.get('new_region')
        if not region:
            co_region = CountryRegion.objects.get(
                slug=self.cleaned_data.get('co_region'))
            region, created = Region.objects.get_or_create(
                name=new_region,
                country_region=co_region)
            self.cleaned_data['region'] = region

        return super(TrailheadForm, self).clean()

HikeFormset = forms.inlineformset_factory(
    Trailhead, Hike,
    form=HikeForm,
    exclude=('trailhead',),
    extra=1, can_delete=False)
