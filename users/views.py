from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import CustomUser, Payments
from users.serializer import (CustomUserDetailSerializer, CustomUserSerializer,
                              PaymentSerializer)
from users.servises import create_product, create_stripe_price, create_session
from rest_framework import generics

class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    # serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)  # Пзволяем создавать пользователей без авторизации

    def get_permissions(self):
        # Получаем список разрешений, в зависимости от типа запроса
        if self.action in ["create"]:  # Если действие - создание пользователя
            permission_classes = (AllowAny,)  # Позволяем всем доступ к этому действию
        else:  # Для остальных действий (retrieve, update, delete и т.д.)
            permission_classes = [permissions.IsAuthenticated]  # Требуем аутентификацию

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # Создаем пользователя с указанными данными и устанавливаем активность
        user = serializer.save(is_active=True)
        # Устанавливаем хешированный пароль
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            user = self.get_object()
            if self.request.user == user:
                # if self.request.user.user_permissions == IsProfileOwner:

                return CustomUserDetailSerializer  # Если пользователь владелец, используем полный сериализатор
            else:
                return CustomUserSerializer  # В противном случае - ограниченный
        return CustomUserSerializer


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


