# coding: utf-8
from django.test import TestCase

from homesite.views import HomeView


class HomeViewTest(TestCase):
    def test_template_name(self):
        view = HomeView()
        self.assertEqual(view.template_name, 'homesite/base.html')
