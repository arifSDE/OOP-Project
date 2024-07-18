import uuid
from product import Product
class Seller:
    def __init__(self, email, password, seller_name):
        self.seller_id = str(uuid.uuid4())  # Unique ID for each seller
        self.email = email
        self.password = password
        self.seller_name = seller_name
        self.products = []
    
    def publish_product(self, product_name, price, stock):
        new_product = Product(product_name, price, stock)
        self.products.append(new_product)
        print(f"Product '{product_name}' published successfully by {self.seller_name}.")
        return new_product
    
    def __str__(self):
        return f"Seller ID: {self.seller_id}, Name: {self.seller_name}"
