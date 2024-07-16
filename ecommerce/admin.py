admin = {'email': 'admin', 'password': 'admin123'}

def admin_menu(products):
    while True:
        print('\n1. Add product\n2. Remove product\n3. View products\n4. Logout')
        admin_choice = int(input('Enter your choice: '))
        if admin_choice == 1:
            id = int(input('Enter product id: '))
            if any(p['id'] == id for p in products):
                print(f"Product with ID {id} already exists. Please use a different ID.")
                continue
            name = input('Enter product name: ')
            price = int(input('Enter product price: '))
            products.append({'id': id, 'name': name, 'price': price})
            print('Product added')
        elif admin_choice == 2:
            id_str = input('Enter product id to remove: ')           
            if not id_str.isdigit():
                print("Invalid input. Please enter a valid number for the product ID.")
                continue  
            id = int(id_str)
            product_to_remove = None
            for product in products:
                if product['id'] == id:
                    product_to_remove = product
                    break
            if product_to_remove:
                products.remove(product_to_remove)
                print('Product removed')
            else:
                print(f"No product found with ID {id}")
        # elif admin_choice == 2:
        #     id = int(input('Enter product id to remove: '))
        #     products = [p for p in products if p['id'] != id]
        #     print('Product removed')
        elif admin_choice == 3:
            display_products(products)
        elif admin_choice == 4:
            print('Logged out')
            break

def display_products(products):
    print("{:<6} {:<15} {:<10}".format('ID', 'Name', 'Price'))
    print('-' * 32)
    for p in products:
        print("{:<6} {:<15} {:<10}".format(p['id'], p['name'], p['price']))