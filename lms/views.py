from rest_framework import generics, viewsets

from lms.models import Course, Lesson
from lms.serializer import CourseSerializer, LessonSerializer

from users.permissions import IsModerator, IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    """viewset модели course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator,)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator,)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (~IsModerator,)
