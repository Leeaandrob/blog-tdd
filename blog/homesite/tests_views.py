# coding: utf-8
from django.test import TestCase

from .views import HomeView
from .models import Post


class HomeViewTest(TestCase):

    def setUp(self):
        self.view = HomeView()

    def test_template_name(self):
        self.assertEqual(self.view.template_name, 'homesite/base.html')

    def test_get_context_data(self):
        esperado = self.view.get_context_data()
        self.assertEqual(esperado.keys(), ['posts', 'view'])

    def test_get_context_data_query_vazia(self):
        resposta = list(self.view.get_context_data()['posts'])
        esperado = list(Post.objects.all())
        self.assertEqual(resposta, esperado)

    def test_get_context_data_com_objeto(self):
        Post.objects.create(titulo='Foo', descricao='bar')
        esperado = Post.objects.all()
        resposta = self.view.get_context_data()['posts']
        self.assertEqual(resposta[0].titulo, esperado[0].titulo)
