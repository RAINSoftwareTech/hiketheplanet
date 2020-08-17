#!/usr/bin/env python
# encoding: utf-8
"""
copyright (c) 2020 RAIN Software Technologies.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

"""
# Imports from Django
from django.db import models

# Local Imports
from core.fields import UpperCaseCharField


class Country(models.Model):
    alpha_2_code = UpperCaseCharField(max_length=2, unique=True)
    english_short_name = models.CharField(max_length=50)


class StateProvince(models.Model):
    country = models.ForeignKey(
        Country,
        related_name='states_provinces',
        on_delete=models.PROTECT
    )
    code = UpperCaseCharField(max_length=2, unique=True)
    name = models.CharField(max_length=30)
