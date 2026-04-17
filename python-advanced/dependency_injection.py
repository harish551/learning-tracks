'''
Dependency Injection

Dependency Injection is a design pattern that allows you to 
decouple the creation of an object from its dependencies.

This promotes loose coupling and makes your code more modular, testable, and maintainable.
'''

class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")


class PaypalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal")

class StripeService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through Stripe")


class OrderService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def place_order(self, amount):
        self.payment_processor.process_payment(amount)

# Using dependency injection to provide the payment processor
paypal_processor = PaypalService()
order_service = OrderService(paypal_processor)
order_service.place_order(100)

stripe_processor = StripeService()
order_service = OrderService(stripe_processor)
order_service.place_order(200)

