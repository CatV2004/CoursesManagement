from django.core.serializers import serialize
from rest_framework import serializers
from .models import Course,Category,Tag, Lesson


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name','create_date','active']


class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, course):
        if course.image:
            requests = self.context.get('request')
            if requests:
                return requests.build_absolute_uri('/static/%s' %course.image.name)
            return '/static/%s' %course.image.name


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

