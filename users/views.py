
from rest_framework import viewsets
from users.serializer import CustomUserSerializer
from users.models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели course"""
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
