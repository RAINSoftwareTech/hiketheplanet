from django import forms
from hikes.models import Hike, Hazards, Sights, Equipment


class HikeForm(forms.Form):

    class Meta:
        model = Hike
        fields = ('difficulty_level_explanation', 'description')