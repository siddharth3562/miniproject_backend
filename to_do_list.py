class User:
    def __init__(self,user_id,name,email,password):
        self.user_id=user_id
        self.name=name
        self.email=email
        self.password=password
        self.tasks=[]

class Task:
    def __init__(self,task_id,description):
        self.task_id=task_id
        self.description=description

class Todolist:
    def __init__(self):
        self.users=[]
        self.current_user=None

    def register(self):
        user_id=int(input('Enter user id: '))
        name=input('Enter your name: ')
        email=input('Enter your email: ')
        password=input('Enter your password: ')
        self.users.append(User(user_id,name,email,password))
        print("registration successful..")

    def login(self):
        email=input('Enter your email: ')
        password=input('Enter your password: ')
        for user in self.users:
            if user.email==email and user.password==password:
                self.current_user=user
                print('login successful...')
                return True
        print('invalid email or password...')
        return False

    def add_task(self):
        task_id=len(self.current_user.tasks) + 1
        description=input('enter task description: ')
        self.current_user.tasks.append(Task(task_id, description))
        print('Task added..')

    def view_tasks(self):
        if not self.current_user.tasks:
            print('No tasks to show.')
            return
        print("{:<5} {:<20}".format('ID','Description'))
        print('-' * 25)
        for task in self.current_user.tasks:
            print("{:<5} {:<20}".format(task.task_id,task.description))

    def delete_task(self):
        task_id=int(input('Enter task id to delete: '))
        for task in self.current_user.tasks:
            if task.task_id==task_id:
                self.current_user.tasks.remove(task)
                print('task deleted..')
                return
        print('task not found!..')

    def logout(self):
        self.current_user=None
        print('logged out...')

    def main(self):
        while True:
            print('\n1.Register\n2.Login')
            choice=int(input('Enter your choice: '))
            if choice==1:
                self.register()
            elif choice==2:
                if self.login():
                    while True:
                        print('\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Logout')
                        choice=int(input('Enter your choice: '))
                        if choice==1:
                            self.add_task()
                        elif choice==2:
                            self.view_tasks()
                        elif choice==3:
                            self.delete_task()
                        elif choice==4:
                            self.logout()
                            break

app = Todolist()
app.main()
