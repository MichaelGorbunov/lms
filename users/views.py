from rest_framework import viewsets,generics

from users.models import CustomUser, Payments
from users.serializer import CustomUserSerializer, PaymentSerializer
from rest_framework.filters import  OrderingFilter


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

class PaymentListView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [ OrderingFilter]
    ordering_fields = ["date_pay"]