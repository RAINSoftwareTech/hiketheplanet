# -*- coding: utf-8 -*-

# Imports from Django
from django import forms
from django.db import models

# Imports from Third Party Modules
from factory import Faker


class TestParentModel(models.Model):
    foo = models.CharField(max_length=15, default=Faker('name'))

    class Meta:
        app_label = 'mixins'


class TestChildModel(models.Model):
    foo = models.ForeignKey(TestParentModel)
    bar = models.CharField(max_length=15, default=Faker('name'))

    class Meta:
        app_label = 'mixins'


class TestParentForm(forms.ModelForm):

    class Meta:
        model = TestParentModel
        fields = ['foo']


TestChildFormset = forms.inlineformset_factory(TestParentModel, TestChildModel,
                                               fields=('bar',))
