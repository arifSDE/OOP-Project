import uuid
class Product:
    def __init__(self, name, price, stock):
        self.product_id = str(uuid.uuid4())  # Unique ID for each product
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Stock: {self.stock}"