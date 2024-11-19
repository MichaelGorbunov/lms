
from rest_framework import viewsets
from lms.serializer import CourseSerializer
from lms.models import Course,Lesson


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
