from user import*
from worker import*
from login import*
while True:
    print('\n1.register as user\n2.register as worker\n3.login')
    ch=int(input('enter your choice: '))
    if ch==1:
        user_reg()
    elif ch==2:
        w_reg()
    elif ch==3:
        log_in()
        




