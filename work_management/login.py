from user import*
from worker import*
def log_in():
    email=input('enter your email: ')
    password=input('enter your password: ')
    if user_log(email,password,):
        print('Logged in as user...')
        user_menu(email)
    elif w_login(email,password):
        print('logged in as worker')
        worker_menu(users)
    else:
        print('Invalid email or password.')
