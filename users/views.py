from rest_framework import viewsets

from users.models import CustomUser, Payments
from users.serializer import CustomUserSerializer, PaymentSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
