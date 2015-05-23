# coding: utf-8
from django.test import TestCase

from homesite.views import HomeView


class HomeViewTest(TestCase):

    def setUp(self):
        self.view = HomeView()

    def test_template_name(self):
        self.assertEqual(self.view.template_name, 'homesite/base.html')

    def test_get_context_data(self):
        esperado = self.view.get_context_data()
        self.assertEqual(esperado.keys(), ['posts', 'view'])
