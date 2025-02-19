from debug_toolbar.toolbar import debug_toolbar_urls
from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)


urlpatterns = [
    path('', include(router.urls))
] + debug_toolbar_urls()