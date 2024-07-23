def user_menu():
    while True:
        print('\n1.View available services\n2.Request service\n3.View requested services\n4.Logout')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            print('\n1.Plumber\n2.Electrician\n3.Constructor\n4.Painting')
# def user_menu(email):
#     while True:
#         print('\n1.View available services\n2.Request service\n3.View requested services\n4.Logout')
#         ch = int(input('Enter your choice: '))
#         if ch == 1:
#             print('\n1.Plumber\n2.Electrician\n3.Constructor\n4.Painting')
#         elif ch==2:
#             req_service(email)
#         elif ch==3:
#             view_req_service(email)
#         elif ch==4:
#             print('Logged out successfully.')
#             break
#         else:
#             print('Invalid choice. Please try again.')           

# def view_req_service(email):
#     for user in users:
#         if user['email'] == email:
#             if 'service_requests' in user and user['service_requests']:
#                 print("Your requested services:")
#                 for service in user['service_requests']:
#                     print(f"- {service}")
#             else:
#                 print("You have not requested any services.")
#             return
#     print("User not found")


# def req_service(email):
#     service = input('Enter the service needed: ')
#     for user in users:
#         if user['email'] == email:
#             if 'service_requests' not in user:
#                 user['service_requests'] = []
#             user['service_requests'].append(service)
#             print('Service requested successfully')
#             return
#     print('User not found')
