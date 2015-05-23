# coding: utf-8
from django.test import TestCase

from .views import HomeView, PostListView
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


class PostListViewTest(TestCase):
    def setUp(self):
        self.view = PostListView()

    def test_template_name(self):
        self.assertEqual(self.view.template_name,
                         'homesite/posts.html')

    def test_model(self):
        esperado = Post
        resposta = self.view.model
        self.assertEqual(resposta, esperado)

    def test_objects_vazio(self):
        resposta = list(Post.objects.all())
        esperado = list(self.view.get_queryset())
        self.assertEqual(resposta, esperado)

    def test_objects(self):
        Post.objects.create(titulo='Foo', descricao='bar')
        resposta = Post.objects.all()
        esperado = self.view.get_queryset()[:1]
        self.assertEqual(resposta[0].titulo, esperado[0].titulo)

