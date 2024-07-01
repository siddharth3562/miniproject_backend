books=['harry potter','the hobbit','game of thrones','lord of the rings']
users=[['a','b',22,'c']]
while True:
    print('\n1.register\n2.login')
    ch=int(input())
    if ch==1:
        name=(input('enter user name'))
        email=(input('enter your email'))
        ph=int(input('enter your phone number'))
        password=(input('enter your password'))
        users.append([name,email,ph,password,])
        print('registration sucessful')
    elif ch==2:
        email=(input('enter your email'))
        password=(input('enter your password'))
        f=0
        for i in users:
            if i[1]==email and i[3]==password:
                f=1
                print('login successful')
                while True:
                    print('\n1.borrow book\n2.return book\n3.check available books\n4.logout')
                    c=int(input('enter your choice'))
                    if c==1:
                        h=int('enter the number of books to borrow')
                        for i in range(h):
                            bk=input('enter the book you want to borrow')
                            if bk in books:
                                books.remove(bk)
                                print(f'You have borrowed "{bk}".')
                            else:
                                print('book not available')
                    elif c==2:
                        bk=(input('enter the book to return'))
                        books.append(bk)
                        print(f'You have returned "{bk}".') 
                    elif c==3:
                        for i in books:
                            print(i)
                    elif c==4:
                        print('logged out')
                        break
        if f==0:                            
            print('invalid email or password')                        

#gpt

# books = ['harry potter', 'the hobbit', 'game of thrones', 'lord of the rings']
# users = [['a', 'b', 22, 'c']]
# borrowed_books = {}  # Dictionary to track borrowed books for each user

# while True:
#     print('\n1. Register\n2. Login')
#     ch = int(input('Enter your choice: '))
    
#     if ch == 1:
#         name = input('Enter user name: ')
#         email = input('Enter your email: ')
#         ph = int(input('Enter your phone number: '))
#         password = input('Enter your password: ')
#         users.append([name, email, ph, password])
#         print('Registration successful.')
    
#     elif ch == 2:
#         email = input('Enter your email: ')
#         password = input('Enter your password: ')
#         f = 0
#         for i in users:
#             if i[1] == email and i[3] == password:
#                 f = 1
#                 print('Login successful.')
                
#                 while True:
#                     print('\n1. Borrow book\n2. Return book\n3. Check available books\n4. View borrowing history\n5. Logout')
#                     c = int(input('Enter your choice: '))
                    
#                     if c == 1:
#                         bk = input('Enter the book you want to borrow: ')
#                         if bk in books:
#                             books.remove(bk)
#                             print(f'You have borrowed "{bk}".')
#                             if email in borrowed_books:
#                                 borrowed_books[email].append(bk)
#                             else:
#                                 borrowed_books[email] = [bk]
#                         else:
#                             print('Book not available.')
                    
#                     elif c == 2:
#                         bk = input('Enter the book to return: ')
#                         if email in borrowed_books and bk in borrowed_books[email]:
#                             borrowed_books[email].remove(bk)
#                             books.append(bk)
#                             print(f'You have returned "{bk}".')
#                         else:
#                             print('You did not borrow this book.')
                    
#                     elif c == 3:
#                         print('Available books:')
#                         for book in books:
#                             print(book)
                    
#                     elif c == 4:
#                         if email in borrowed_books and borrowed_books[email]:
#                             print('Your borrowing history:')
#                             for book in borrowed_books[email]:
#                                 print(book)
#                         else:
#                             print('You have not borrowed any books.')
                    
#                     elif c == 5:
#                         print('Logged out.')
#                         break
                    
#                     else:
#                         print('Invalid choice. Please try again.')
        
#         if f == 0:
#             print('Invalid email or password.')
