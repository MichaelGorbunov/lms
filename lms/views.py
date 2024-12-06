from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from lms.models import Course, Lesson, Subscription
from lms.paginators import CoursePaginator, LessonPaginator
from lms.serializer import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModerator, IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
    """viewset модели course"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        # Проверяем, состоит ли пользователь в группе "Модераторы"
        if user.groups.filter(name="Moderators").exists():
            # Если состоит, возвращаем весь queryset
            return Course.objects.all()
        else:
            # Если не состоит, фильтруем по owner
            return Course.objects.filter(owner=user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]

        elif self.action in ['destroy']:
            # self.permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['list']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]

        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        ~IsModerator,
    )

    # permission_classes = ( ~IsModerator,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator, IsOwner)
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner)


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        sub_item = Subscription.objects.all().filter(user=user).filter(course=course)

        if sub_item.exists():
            sub_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course)
            message = "Подписка добавлена"
        return Response({"message": message})
