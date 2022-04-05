"""OKA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from OKA import settings
from main.views import StaticView, SetView, EventView, MapView


urlpatterns = [
    path('', MapView.as_view(), name='map'),

    path('event/<id>', EventView.as_view(), name='current_event'),

    path('about/', StaticView.as_view(), name='about'),
    path('region/', StaticView.as_view(), name='region'),
    path('results/', StaticView.as_view(), name='results'),
    path('archive/', StaticView.as_view(), name='archive'),
    path('contact/', StaticView.as_view(), name='contact'),

    path('team/', SetView.as_view(), name='team'),
    path('event/', SetView.as_view(), name='event'),
    path('update/', SetView.as_view(), name='update'),
]
