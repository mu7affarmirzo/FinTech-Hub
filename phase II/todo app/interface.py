from todos import ToDos, ToDosList
from users import Users, UsersList


todo1 = ToDos('Title 1', 'Description 1')
todo2 = ToDos('Title 2', 'Description 2')
todo3 = ToDos('Title 3', 'Description 3')
todo4 = ToDos('Title 4', 'Description 4')

todolist = ToDosList()
todolist.add_todos(todo1)
todolist.add_todos(todo2)
todolist.add_todos(todo3)
todolist.add_todos(todo4)

todolist.get_list()
#
# todo4.update_todo()

user1 = Users("Bobur1", "Murodov", "+998955550055", "bobur@gmail.com")
user1.add_todo(todo1)
user1.add_todo(todo2)
user1.add_todo(todo3)
user1.get_list_todos()


def main_interface():
    print('')