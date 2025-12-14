# service.py

class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def is_configured(self):
        """Checks if the API key is set."""
        return self.api_key is not None

    def charge(self, amount, currency="USD"):
        """Charges the customer a certain amount."""
        print(f"Charging {amount} {currency}...")
        # In a real application, this would make an API call.
        return {"status": "success", "amount": amount}

def process_payment(amount, processor):
    """

    Processes a payment using a PaymentProcessor.
    """

    if not processor.is_configured:
        raise ValueError("Payment processor is not configured.")

    return processor.charge(amount)
