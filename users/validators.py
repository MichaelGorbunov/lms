from rest_framework.exceptions import ValidationError


class PaymentValidator:

    def __init__(self, fields: list):
        self.fields = fields

    def __call__(self, value):
        values = dict(value)
        tmp = [values.get(x) for x in self.fields]

        if not any(tmp):
            raise ValidationError("Вы должны выбрать урок или курс для оплаты")
