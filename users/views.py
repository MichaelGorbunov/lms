from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from users.models import CustomUser, Payments
from users.serializer import CustomUserSerializer, PaymentSerializer
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    # permission_classes = [AllowAny]  # Позволяем создавать пользователей без авторизации

    def perform_create(self, serializer):
        # Создаем пользователя с указанными данными и устанавливаем активность
        user = serializer.save(is_active=True)
        # Устанавливаем хешированный пароль
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        # Получаем список разрешений, в зависимости от типа запроса
        if self.action in ['create']:  # Если действие - создание пользователя
            permission_classes = [permissions.AllowAny]  # Позволяем всем доступ к этому действию
        else:  # Для остальных действий (retrieve, update, delete и т.д.)
            permission_classes = [permissions.IsAuthenticated]  # Требуем аутентификацию

        return [permission() for permission in permission_classes]


class PaymentsViewSet(viewsets.ModelViewSet):
    """работа с платежами"""
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()


class PaymentListView(generics.ListAPIView):
    """вывод списка платежей"""
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["date_pay"]
    filterset_fields = ["pay_type", "pay_course", "pay_lesson"]
