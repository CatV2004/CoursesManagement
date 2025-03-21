from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', null=True)


class BaseModel(models.Model):
    create_date = models.DateField(auto_now_add=True, null = True)
    update_date = models.DateField(auto_now=True, null = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']

class Category(BaseModel):
    name = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length = 255, null = False)
    description = RichTextField()

    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_query_name='courses')
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')


class Lesson(BaseModel):
    subject = models.CharField(max_length = 255, null = False)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_query_name='lessons')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class rating(BaseModel):
    pass