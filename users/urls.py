from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import CustomUserViewSet,PaymentsViewSet,PaymentListView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", CustomUserViewSet, basename="user")
router.register(r"pay",PaymentsViewSet,basename="pay")

urlpatterns = [
                  path("pay_list/", PaymentListView.as_view(), name="pay-list"),
              ] + router.urls
