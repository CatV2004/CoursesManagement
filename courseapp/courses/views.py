from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from courses.models import Course
from courses.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]