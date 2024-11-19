from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet
from django.urls import path


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", CustomUserViewSet, basename="user")

urlpatterns = [

              ] + router.urls