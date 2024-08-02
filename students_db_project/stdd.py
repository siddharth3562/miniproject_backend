import mysql.connector

std = mysql.connector.connect(
    host="localhost",
    user="siddharth", 
    password="@sidhu2003",  
    database="std_database"  
)

cursor=std.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        std_id INT,
        name text,
        email Varchar(100),
        ph_no VARCHAR(100),
        place VARCHAR(100)
    )
# ''')

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all')
    ch = int(input('enter your choice: '))
    if ch == 1:
        id = int(input('enter employee id: '))
        name = input('enter your name: ')
        email = input('enter your email: ')
        phone = input('enter phone number: ')
        place = input('enter your place: ')
        cursor.execute('INSERT INTO students (std_id, name, email, ph_no, place) VALUES (%s, %s, %s, %s, %s)',
                       (id, name, email, phone, place))
        std.commit()
    elif ch == 2:
        id = int(input('enter employee id: '))
        name = input('enter your name: ')
        email = input('enter your email: ')
        phone = input('enter phone number: ')
        place = input('enter your place: ')
        cursor.execute('UPDATE students SET name=%s, email=%s, ph_no=%s, place=%s WHERE std_id=%s',
                       (name, email, phone, place, id))
        std.commit()
    elif ch == 3:
        id = int(input('enter id of student to delete: '))
        cursor.execute('DELETE FROM students WHERE std_id=%s', (id,))
        std.commit()
    elif ch == 4:
        id = int(input('enter id to search: '))
        cursor.execute('SELECT * FROM students WHERE std_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<20}{:<20}{:<10}'.format('id', 'name', 'email', 'phone', 'place'))
        print('-' * 75)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<20}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('id not available')
    elif ch == 5:
        cursor.execute('SELECT * FROM students')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<20}{:<20}{:<10}'.format('id', 'name', 'email', 'phone', 'place'))
        print('-' *75)
        for i in data:
            print("{:<10}{:<10}{:<20}{:<20}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))