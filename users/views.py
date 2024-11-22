from rest_framework import viewsets

from users.models import CustomUser
from users.serializer import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
