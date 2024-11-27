from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from users.models import CustomUser, Payments
from users.serializer import CustomUserSerializer, PaymentSerializer
from rest_framework.filters import OrderingFilter


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


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
