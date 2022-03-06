class ToDosList:
    def __init__(self):
        self.todos_list = []

    def add_todos(self, todo_obj):
        self.todos_list.append(todo_obj)

    def delete_todo(self, todo_obj):
        if todo_obj in self.todos_list:
            self.todos_list.remove(todo_obj)
            print(f'{todo_obj.title} successfully deleted!')

    def get_list(self):
        if not self.todos_list:
            print("There is no todos")
        for todo in self.todos_list:
            todo.get_todo_info()


class ToDos:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_todo_info(self):
        print(f'Title: {self.title}')
        print(f'Description: {self.description}\n')

    def update_todo(self):
        title = input("Updated title:")
        self.title = title
        description = input("Updated description:")
        self.description = description

        print('Updated info of the ToDo')
        self.get_todo_info()
    #
    # def get_list(self):
    #     pass

# todo1 = ToDos('Title 1', 'Description 1')
# todo2 = ToDos('Title 2', 'Description 2')
# todo3 = ToDos('Title 3', 'Description 3')
# todo4 = ToDos('Title 4', 'Description 4')

# todolist = ToDosList()
# todolist.add_todos(todo1)
# todolist.add_todos(todo2)
# todolist.add_todos(todo3)
# todolist.add_todos(todo4)
#
# todolist.get_list()
# todolist.delete_todo(todo2)
# todolist.get_list()

# todo4.update_todo()