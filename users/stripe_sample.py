import stripe
import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


stripe.api_key = os.getenv("STRIPE_API_KEY")
# stripe.Product.create(name="Gold Plan")
# print(stripe.Balance.retrieve())
stripe.Price.create(
  currency="usd",
  unit_amount=1000,

  product_data={"name": "Gold Plan"},
)
# stripe.PaymentLink.create(
#   line_items=[{"price": "price_1QSyJbErjaeIfcDQN08PnBV8", "quantity": 1}],
# )

print(stripe.Price.list())