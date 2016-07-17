"""djangocon_drf_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from quick.views import UserView
from pokemon.views import PokemonView, TeamView, TrainerView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('users', UserView)
router.register('pokemon', PokemonView)
# router.register('teams', TeamView)
# router.register('trainers', TrainerView)

ListCreateMapper = {
    'get': 'list',
    'post': 'create',
}

RetrieveUpdateDestroyMapper = {
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
    'put': 'update',
}

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^teams/$', TeamView.as_view(ListCreateMapper)),
    url(r'^teams/(?P<pk>[0-9]+)/$', TeamView.as_view(RetrieveUpdateDestroyMapper)),
    url(r'^teams/(?P<pk>[0-9]+)/trainers/$', TrainerView.as_view(RetrieveUpdateDestroyMapper)),
    url(r'^teams/(?P<team_pk>[0-9]+)/trainers/(?P<pk>[0-9]+)$', 
        TrainerView.as_view(RetrieveUpdateDestroyMapper)),
]
