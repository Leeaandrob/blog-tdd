from django.conf.urls import include, url
from django.contrib import admin

from homesite.views import HomeView
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(regex=r'^$', view=HomeView.as_view(), name='home')
]
