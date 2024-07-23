workers=[]

def w_reg():
    w_name=input('enter your name: ')
    w_email=input('enter your email: ')
    skill=input('enter your skill: ')
    w_password=input('enter your password: ')
    workers.append({'name':w_name,'email':w_email,'skill':skill,'password':w_password})

def w_login(w_email,w_password):
    for worker in workers:
        if worker['email']==w_email and worker['password']==w_password:
            return True  
    return False 

def worker_menu(users):
    while True:
        print('\n1.View requests\n2.Logout')
        ch = int(input('Enter your choice: '))
        if ch==1:
            view_requests(users)
        elif ch==2:
            print('logged out')
            break

            
def view_requests(users):
    print("All service requests:")
    print("{:<6} {:<15} {:<10}".format('Name', 'email', 'phone no.'))
    print('-' * 32)
    for i in users:
            print("{:<6} {:<15} {:<10}".format(i['name'], i['email'], i['phone']))

