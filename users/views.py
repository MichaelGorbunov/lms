
from rest_framework import viewsets
from users.serializer import CustomUserSerializer
from users.models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
