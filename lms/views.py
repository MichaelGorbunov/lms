from rest_framework import generics, viewsets

from lms.models import Course, Lesson
from lms.serializer import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """viewset модели course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    # books_with_authors = Book.objects.select_related('author').all()
    queryset = Lesson.objects.select_related("course").all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
