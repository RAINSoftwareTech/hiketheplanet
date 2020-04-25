# -*- coding: utf-8 -*-

from django.template import Template, Context
from django.test import TestCase


class HikeTemplateTagsTests(TestCase):
    TEMPLATE = Template("{% load hike_tags %} "
                        "{% kwargs_url 'hikes:broad_region_home' params %}")

    def test_kwargs_url(self):
        params = {'co_region_slug': 'region-slug'}
        rendered = self.TEMPLATE.render(Context({'params': params}))
        self.assertIn('region-slug', rendered)
