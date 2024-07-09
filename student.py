students=[]
admin={'email':'admin','password':'admin123'}
course=[{'id':11,'sub':'mern stack'},{'id':22,'sub':'python'},{'id':33,'sub':'data science'}]
while True:
    print('\n1.register\n2.login')
    ch=int(input('enter your choice: '))
    if ch==1:
        id=int(input('enter student id: '))
        sname=input('enter your name: ')
        email=input('enter your email: ')
        spass=input('enter your password: ')
        students.append({'id':id,'name':sname,'email':email,'password':spass,'course':None,'grade':None})
    elif ch==2:
        email=(input('enter your email: '))
        password=(input('enter your password: '))
        f=0
        if admin['email']==email and admin['password']==password:
            f=1
            print('login as admin') 
            while True:
                    print('\n1.give grade\n2.view students\n3.logout')
                    c=int(input('enter your choice: '))
                    if c==1:
                        id=int(input('enter the id of student to input grade: '))
                        grade=input('enter the grade: ')
                        for i in students:
                            if i['id']==id:
                                i['grade']=grade
                                print('grade assigned')
                            else:
                                print("Student ID not found")                 
                    elif c==2:
                        print("{:<10}{:<9}{:<9}{:<12}{:<9}".format('id','name','email','course','grade'))
                        print('_'*50)
                        for i in students:
                            print("{:<10}{:<9}{:<9}{:<12}{:<9}".format(i['id'],i['name'],i['email'],i['course'] if i['course'] else 'None',i['grade'] if i['grade'] else 'None'))                  
                    elif c==3:
                        print('logged out')
                        break
        for student in students:
            if student['email']==email and student['password']==password:
                f=1
                print('login successful')
                while True:
                    print('\n1.view available courses\n2.enroll in course\n3.view grades\n4.logout')
                    c=int(input('enter your choice: '))
                    if c==1:
                        print("{:<6}{:<9}".format('id','course'))
                        print('_'*20)
                        for i in course:
                            print("{:<6}{:<9}".format(i['id'],i['sub']))   
                    elif c==2:
                        id=int(input('enter the course id you want to enroll in: '))
                        course_name = None
                        for crs in course:
                            if crs['id'] == id:
                                course_name = crs['sub']
                                break
                        if course_name:
                            student['course'] = course_name
                            print(f"Enrolled in course: {course_name}")
                        else:
                            print("Invalid course ID")
                    elif c==3:
                        print("{:<10}{:<15}{:<10}".format('id','Course','Grade'))
                        print('_'*30)
                        print("{:<10}{:<15}{:<10}".format(student['id'], student['course'] if student['course'] else 'None', student['grade'] if student['grade'] else 'None'))
                    elif c==4:
                        print('logged out')
                        break







    


    
