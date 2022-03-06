

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
        for count, value in enumerate(self.todos):
            print(count, value)


class ToDos:
    def __init__(self):
        pass

    def create_todo(self):
        pass

    def delete_todo(self):
        pass

    def update_todo(self):
        pass

    def get_list(self):
        pass


def get_users_list(obj):
    obj.get_user_info()


def get_todos_list():
    print("All the todos")


def main_view():
    print("Hello, choose your option:")
    print("1. Users list")
    print("2. ToDos list")

    all_choices = {1: get_users_list, 2: get_todos_list}
    choice = int(input("Your option:"))
    if choice == 1:
        x = all_choices[choice]
        x()
    elif choice == 2:
        x = all_choices[choice]
        x()
    else:
        while choice != 1 and choice != 2:
            choice = int(input("Siz faqat yo birinchi yo ikkinchi tanlovni tanlashingiz mumkin"))
        x = all_choices[choice]
        x()

user1 = Users("Bobur", "Murodov", "+998955550055", "bobur@gmail.com")
user2 = Users("Bobur", "Murodov", "+998955550055", "bobur@gmail.com")
user3 = Users("Bobur", "Murodov", "+998955550055", "bobur@gmail.com")
user4 = Users("Bobur", "Murodov", "+998955550055", "bobur@gmail.com")
user5 = Users("Bobur", "Murodov", "+998955550055", "bobur@gmail.com")
# user1.__init__("Toshmat",None,None,None)-
# user1.get_user_info()

userlist = UsersList()
userlist.add_users(user1)
userlist.add_users(user2)
userlist.add_users(user3)
userlist.add_users(user4)
userlist.add_users(user5)
userlist.show_users()
userlist.del_user(user1)
userlist.del_user(user5)
userlist.del_user(user3)
userlist.show_users()
# main_view()
