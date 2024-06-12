import pprint
todo_list = []
class Task:
    def __init__(self, title, desc, priority, due_date):
        self.title = title
        self.desc = desc
        self.priority = priority
        self.due_date = due_date


todo = Task('Hakdog', 'Make Hakdog', 'High', 'Today')
todo1 = Task('Hakdog1', 'Make Hakdog2', 'High', 'Today')

todo_list = [todo, todo1]

import shelve

def save_todo():
    save = shelve.open('todo')
    save['todo'] = todo_list
    save.close()

def load_todo():
    load = shelve.open('todo')
    todo_list = load['todo']
    load.close()

    print(todo_list[2].title)
#save_todo()

#load_todo()

del todo_list[0]
print(todo_list)




