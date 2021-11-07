# Imports from Django
from django.db.models import CharField


class UpperCaseCharField(CharField):
    """CharField that ensures data is saved as uppercase"""

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            value = str(value).upper()
        return value