from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import CustomUserViewSet,PaymentsViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", CustomUserViewSet, basename="user")
router.register(r"pay",PaymentsViewSet,basename="pay")

urlpatterns = [] + router.urls
