from debug_toolbar.toolbar import debug_toolbar_urls
from django.template.defaulttags import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
] + debug_toolbar_urls()