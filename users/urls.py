from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (CustomUserViewSet, PaymentListView, PaymentsViewSet)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", CustomUserViewSet, basename="user")
router.register(r"pay", PaymentsViewSet, basename="pay")

urlpatterns = [
    path("pay_list/", PaymentListView.as_view(), name="pay-list"),
    path(
        "user/login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),



] + router.urls
