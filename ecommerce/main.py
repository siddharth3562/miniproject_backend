from admin import*
from user import*
from product import*

while True:
        print('\n1. Register\n2. Login')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            register_user()
        elif choice == 2:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            if admin['email'] == email and admin['password'] == password:
                print('Logged in as admin')
                admin_menu(products)
            else:
                login_user(email, password, products)
    


    
