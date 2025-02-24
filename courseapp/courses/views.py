from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from courses.models import Course, Category
from courses import serializers
from courses import paginators
from rest_framework.response import Response


# Create your views here.
class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')

        if q:
            queries = queries.filter(subject__icontains = q)

        return queries

    @action(methods=['get'], detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active = True).all()

        return Response(serializers.LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]