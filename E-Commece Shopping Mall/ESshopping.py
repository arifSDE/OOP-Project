from customer import Customer
from seller import Seller

class EShoppingApp:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []
        self.orders = []
    
    def create_customer_account(self, email, password):
        for customer in self.customers:
            if customer.email == email:
                print("Account creation failed. Email already exists.")
                return
        new_customer = Customer(email, password)
        self.customers.append(new_customer)
        print("Customer account created successfully.")
        return new_customer
    
    def create_seller_account(self, email, password, seller_name):
        for seller in self.sellers:
            if seller.email == email:
                print("Account creation failed. Email already exists.")
                return
        new_seller = Seller(email, password, seller_name)
        self.sellers.append(new_seller)
        print("Seller account created successfully.")
        return new_seller
    
    def publish_product(self, seller_email, product_name, price, stock):
        for seller in self.sellers:
            if seller.email == seller_email:
                new_product = seller.publish_product(product_name, price, stock)
                self.products.append(new_product)
                return new_product
        print("Publishing product failed. Seller not found.")
        return None
    
    def list_all_products(self):
        print("All available products:")
        for product in self.products:
            if product.stock > 0:
                print(product)
    
    def add_product_to_cart(self, customer_email, product_id, quantity=1):
        for customer in self.customers:
            if customer.email == customer_email:
                for product in self.products:
                    if product.product_id == product_id:
                        if product.stock >= quantity:
                            customer.add_to_cart(product, quantity)
                        else:
                            print(f"'{product.name}' is out of stock. Cannot add to cart.")
                        return
                print("Product not found.")
                return
        print("Customer not found.")
    
    def place_order(self, customer_email):
        for customer in self.customers:
            if customer.email == customer_email:
                order = customer.place_order()
                if order:
                    self.orders.append(order)
                    return order
                return None
        print("Customer not found.")
        return None
    
    def list_all_orders(self):
        print("All orders:")
        for order in self.orders:
            print(order)
