from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from courses import dao
class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request,
                            'admin/stats.html', {
                            'stats': dao.count_courses_by_cate()
                            })

admin_site = CourseAppAdminSite(name='myadmin')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class TagInLineCourse(admin.StackedInline):
    model = Course.tags.through
    extra = 1
    verbose_name = "Tag của khóa học"
    verbose_name_plural = "Danh sách Tags của khóa học"


class TagInLineLesson(admin.StackedInline):
    model = Lesson.tags.through
    extra = 1
    verbose_name = "Tag của bài học"
    verbose_name_plural = "Danh sách Tags của bài học"


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']
    inlines = [TagInLineCourse]
    form = CourseForm
    exclude = ['tags']

    def img(self, Course):
        if Course:
            return mark_safe(
                '<img src="/static/{url}" width = "120" />'.format(url=Course.image.name)
            )

    class Media:
        css = {
            'all':('/static/css/style.css',)
        }


class LessonAdmin(admin.ModelAdmin):
    form = CourseForm
    inlines = [TagInLineLesson]
    exclude = ['tags']


# Register your models here.
admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag)


