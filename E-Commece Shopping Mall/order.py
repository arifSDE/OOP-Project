import uuid
class Order:
    def __init__(self, customer, products, total_amount):
        self.order_id = str(uuid.uuid4())  # Unique ID for each order
        self.customer = customer
        self.products = products
        self.total_amount = total_amount
    
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.email}, Total Amount: ${self.total_amount}"