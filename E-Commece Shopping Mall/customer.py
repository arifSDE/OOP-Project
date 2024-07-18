import uuid
from order import Order
class Customer:
    def __init__(self, email, password):
        self.customer_id = str(uuid.uuid4())  
        self.email = email
        self.password = password
        self.cart = []
    def add_to_cart(self, product, quantity=1):
        self.cart.append((product, quantity))
        print(f"Added {quantity} '{product.name}' to cart.")
    def place_order(self):
        if not self.cart:
            print("Your cart is empty. Add some products to place an order.")
            return
        
        for product, quantity in self.cart:
            if product.stock >= quantity:
                product.stock -= quantity
            else:
                print(f"Cannot place order. '{product.name}' is out of stock.")
                return
        
        total_amount = sum(product.price * quantity for product, quantity in self.cart)
        order = Order(self, self.cart, total_amount)
        print(f"Order placed successfully. Order ID: {order.order_id}")
        self.cart = []  # Clear the cart after placing the order
        return order
    
    def __str__(self):
        return f"Customer ID: {self.customer_id}, Email: {self.email}"