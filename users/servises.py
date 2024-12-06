import stripe
from config.settings import STRIPE_API_KEY
from lms.models import Lesson, Course

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount, product_id):
    """Получение цены для stripe на основе """

    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product_id
    )

    return stripe_price


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get('url')


def create_product(item: Lesson | Course):

    product = stripe.Product.create(
        name=item.title,
        description=item.description
    )
    return product.get("id")