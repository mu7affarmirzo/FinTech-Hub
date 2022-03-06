class UsersList:
    def __init__(self):
        self.users_list = []

    def add_users(self, user_obj): #foydalanuvchi qo'shadi
        self.users_list.append(user_obj)

    def show_users(self):#hamma foydalanuvchilarni korsatadi
        if not self.users_list:
            print("There is no users")
        for user in self.users_list:
            user.get_user_info()

    def del_user(self, user):# foydalanuvchini royxatdan olib tashlaydi
        self.users_list.remove(user)


class Users:
    def __init__(self, f_name, l_name, number, email):
        self.f_name = f_name
        self.l_name = l_name
        self.number = number
        self.email = email
        self.todos = []

    def get_user_info(self):
        print(f'{self.f_name} {self.l_name}\nNumber: {self.number}')
        print(f'Email: {self.email}\n')

    def update_user_info(self):
        f_name = input("Updated first name:")
        self.f_name = f_name
        l_name = input("Updated last name:")
        self.l_name = l_name
        number = input("Updated number:")
        self.number = number
        email = input("Updated email:")
        self.email = email
        print('Successfully update!\nNew updated info:')
        self.get_user_info()

    def add_todo(self, obj):
        self.todos.append(obj)

    def get_list_todos(self):
        if not self.todos:
            print("There is no todo")
        for count, value in enumerate(self.todos):
            print(count, value.get_todo_info())

# user1 = Users("Bobur1", "Murodov", "+998955550055", "bobur@gmail.com")
# user2 = Users("Bobur2", "Murodov", "+998955550055", "bobur@gmail.com")
# user3 = Users("Bobur3", "Murodov", "+998955550055", "bobur@gmail.com")
# user4 = Users("Bobur4", "Murodov", "+998955550055", "bobur@gmail.com")
# user5 = Users("Bobur5", "Murodov", "+998955550055", "bobur@gmail.com")
#
# userlist = UsersList()
# userlist.add_users(user1)
# userlist.add_users(user2)
# userlist.add_users(user3)
# userlist.add_users(user4)
# userlist.add_users(user5)
# userlist.show_users()
#
# print('************************** some Users are deleted*************')
#
# userlist.del_user(user1)
# userlist.del_user(user5)
# userlist.del_user(user3)
# userlist.show_users()
# user1.get_list_todos()

# user4.update_user_info()