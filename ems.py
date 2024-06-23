emp=[[1,'achu',21,500,0,'achu2003@gmail.com',8281434986]]
while True:
    print("1.add,\n2.view\n3.update\n4.delete")
    choice=int(input('enter your choice'))
    if choice==1:
        emp_id=int(input('enter your id'))
        emp_name=str(input('enter your name'))
        emp_age=int(input('enter your age'))
        emp_salary=int(input('enter your salary'))
        emp_exp=int(input('enter your experience'))
        emp_email=input('enter your email')
        emp_phno=int(input('enter your phn no.'))
        emp.append([emp_id,emp_name,emp_age,emp_salary,emp_exp,emp_email,emp_phno])
    elif choice==2:
        for i in emp:
            print('id:',i[0])
            print('name:',i[1])
            print('age:',i[2])
            print('salary:',i[3])
            print('experience:',i[4])
            print('email:',i[5])
            print('phone no:',i[6])
    elif choice==3:
        id=int(input('enter your id'))
        f=0
        for i in emp:
            if id==i[0]:
                f=1
                emp_name=str(input('enter your name'))
                emp_age=int(input('enter your age'))
                emp_salary=int(input('enter your salary'))
                emp_exp=int(input('enter your experience'))
                i[1]=emp_name
                i[2]=emp_age
                i[3]=emp_salary
                i[4]=emp_exp
        if f==0:
            print('ivalid id')
            




