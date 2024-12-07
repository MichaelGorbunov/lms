from rest_framework import serializers

from users.models import CustomUser, Payments
from users.validators import PaymentValidator


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
        validators = [
            PaymentValidator(fields=["pay_lesson", "pay_course"]),
        ]


class CustomUserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    payment_list = PaymentSerializer(many=True, read_only=True, source="pays")

    # payment_list = serializers.SerializerMethodField(read_only=True)
    # def get_payment_list(self, customuser):
    #     return [payment.date_pay for payment in Payments.objects.filter(user_pay=customuser)]

    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = "username", "email", "password"
