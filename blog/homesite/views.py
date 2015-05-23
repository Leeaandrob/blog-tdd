# coding: utf-8
from django.views.generic import TemplateView

from .models import Post


class HomeView(TemplateView):
    template_name = 'homesite/base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
