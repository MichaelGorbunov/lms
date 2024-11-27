from rest_framework import generics, viewsets

from lms.models import Course, Lesson
from lms.serializer import CourseSerializer, LessonSerializer

from users.permissions import IsModerator, IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    """viewset модели course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        # Проверяем, состоит ли пользователь в группе "Модераторы"
        if user.groups.filter(name='Moderators').exists():
            # Если состоит, возвращаем весь queryset
            return Course.objects.all()
        else:
            # Если не состоит, фильтруем по owner
            return Course.objects.filter(owner=user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator,)

    # permission_classes = ( ~IsModerator,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModerator, IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner)
