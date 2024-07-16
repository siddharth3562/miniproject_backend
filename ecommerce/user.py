users = []

def register_user():
    id = int(input('Enter user id: '))
    uname = input('Enter your name: ')
    email = input('Enter your email: ')
    upass = input('Enter your password: ')
    users.append({'id': id, 'name': uname, 'email': email, 'password': upass, 'cart': []})
    print("Registration successful")

def login_user(email, password, products):
    for user in users:
        if user['email'] == email and user['password'] == password:
            print('Login successful')
            user_menu(user, products)
            return True
    return False

def user_menu(user, products):
    while True:
        print('\n1. View products\n2. Add to cart\n3. View cart\n4. Logout')
        user_choice = int(input('Enter your choice: '))
        if user_choice == 1:
            display_products(products)
        elif user_choice == 2:
            id = int(input('Enter product id to add to cart: '))
            product = next((p for p in products if p['id'] == id), None)
            if product:
                user['cart'].append(product)
                print(f"Added {product['name']} to cart")
            else:
                print("Invalid product ID")
        elif user_choice == 3:
            print("{:<6} {:<15} {:<10}".format('ID', 'Name', 'Price'))
            print('-' * 32)
            for item in user['cart']:
                print("{:<6} {:<15} {:<10}".format(item['id'], item['name'], item['price']))
        elif user_choice == 4:
            print('Logged out')
            break

def display_products(products):
    print("{:<6} {:<15} {:<10}".format('ID', 'Name', 'Price'))
    print('-' * 32)
    for p in products:
        print("{:<6} {:<15} {:<10}".format(p['id'], p['name'], p['price']))
