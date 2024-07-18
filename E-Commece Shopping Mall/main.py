
from customer import Customer
from ESshopping import EShoppingApp
from order import Order
from product import Product
from seller import Seller

def main():
    app = EShoppingApp()
    
    while True:
        print("\nWelcome to E-Shopping App!")
        print("1. Create Customer Account")
        print("2. Create Seller Account")
        print("3. Login as Customer")
        print("4. Login as Seller")
        print("5. Publish Product")
        print("6. List All Products")
        print("7. Add Product to Cart")
        print("8. Place Order")
        print("9. List All Orders")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            email = input("Enter email: ")
            password = input("Enter password: ")
            app.create_customer_account(email, password)
        
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            seller_name = input("Enter seller name: ")
            app.create_seller_account(email, password, seller_name)
        
        elif choice == '3':
            email = input("Enter customer email: ")
            password = input("Enter password: ")
            # Implement login functionality for customers
            
        elif choice == '4':
            email = input("Enter seller email: ")
            password = input("Enter password: ")
            # Implement login functionality for sellers
            
        elif choice == '5':
            if not app.sellers:
                print("No sellers available. Please create a seller account first.")
                continue
            
            seller_email = input("Enter seller email: ")
            product_name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter initial stock: "))
            app.publish_product(seller_email, product_name, price, stock)
        
        elif choice == '6':
            app.list_all_products()
        
        elif choice == '7':
            if not app.customers:
                print("No customers available. Please create a customer account first.")
                continue
            
            customer_email = input("Enter customer email: ")
            product_id = input("Enter product ID to add to cart: ")
            quantity = int(input("Enter quantity: "))
            app.add_product_to_cart(customer_email, product_id, quantity)
        
        elif choice == '8':
            if not app.customers:
                print("No customers available. Please create a customer account first.")
                continue
            
            customer_email = input("Enter customer email: ")
            app.place_order(customer_email)
        
        elif choice == '9':
            app.list_all_orders()
        
        elif choice == '0':
            print("Thank you for using E-Shopping App!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
