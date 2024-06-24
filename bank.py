user=[['achu',28392,'a','b',0]]
while True:
    print("\n1.register\n2.login")
    choice=int(input('enter your choice'))
    if choice==1:
        name=str(input('enter your name'))
        phone=int(input('enter your phone number'))
        email=input('enter your email')
        password=input('enter your password')
        user.append([name,phone,email,password,0])
        print(user)
    elif choice==2:
        email=input('enter your email')
        password=input('enter your password')
        f=0
        for i in user:
            if i[2]==email and i[3]==password:
                f=1
                print('login successful')
                while True:
                    print('\n1.balance\n2.deposit\n3.withdraw\n4.logout')
                    ch=int(input('enter your choice'))
                    if ch==1:
                        print('balance',i[4])
                    elif ch==2:
                        deposit=int(input('enter amount to deposit'))
                        i[4]+=deposit
                        print('amount:',deposit)
                    elif ch==3:
                        withdraw=int(input('enter amount to withdraw'))
                        if withdraw>i[4]:
                            print('insufficient cash')
                        else:
                            i[4]-=withdraw
                    elif ch==4:
                        print('logged out')
                        break
        if f==0:
            print('invalid email or password')
