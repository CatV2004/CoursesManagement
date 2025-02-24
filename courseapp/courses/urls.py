from debug_toolbar.toolbar import debug_toolbar_urls
from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='courses')
router.register('categories', views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls))
] + debug_toolbar_urls()