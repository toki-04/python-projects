#! python3 
# cli-todo.py - A simple CLI TODO APP

import curses
from curses import textpad
import shelve

class Task:
    def __init__(self, title, desc, priority, due_date):
        self.title = title
        self.desc = desc
        self.priority = priority
        self.due_date = due_date

def save_todo(todo):
    save = shelve.open('todo')
    save['todo'] = todo 
    save.close()

def load_todo():
    load = shelve.open('todo')
    todo = load['todo']
    load.close()

    return todo


todo_list = load_todo()

def print_title(stdscr):
    title_text = 'CLI TODO APP'

    sh, sw = stdscr.getmaxyx()
    x = sw//2 - len(title_text) //2
    y = sh//2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(1, 2, title_text, curses.A_BOLD)
    num_of_todo_str = f'TODO\'s: {len(todo_list)}'
    stdscr.addstr(1, (sw-len(num_of_todo_str)-2), num_of_todo_str, curses.A_BOLD)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def print_todo(stdscr):

    sh, sw = stdscr.getmaxyx()
    x = sw - 2
    y = sh - 3

    textpad.rectangle(stdscr, 2, 1, y, x)

    start_x = 3
    for idx, todo in enumerate(todo_list):
        idx += 1
        start_y = 4 * idx - 2

        textpad.rectangle(stdscr, start_y+1, start_x, start_y+4, x-2)
        title_str = f' {idx}. {todo.title} '
        stdscr.addstr(start_y+1, start_x+2, title_str, curses.A_BOLD)

        color_pair = 0
        if todo.priority.lower() == 'high':
            color_pair = 1
        elif todo.priority.lower() == 'low':
            color_pair = 3
        else:
            color_pair = 2

        due_date_str = f' Due-Date: {todo.due_date} '
        center = sw//2 - len(due_date_str)//2
        #stdscr.addstr(start_y+4, center, due_date_str)

        stdscr.attron(curses.color_pair(color_pair))
        priority_str = f' Priority: {todo.priority} '
        stdscr.addstr(start_y+1, (x-(len(priority_str))-3), priority_str)
        stdscr.attroff(curses.color_pair(color_pair))

        desc_str = f'{todo.desc}'
        stdscr.addstr(start_y+2, start_x+2, desc_str)

    stdscr.refresh()

def add_todo(stdscr):
    sh, sw = stdscr.getmaxyx()

    if sw > 50:
        sw = 50

    stdscr.clear()

    # Title
    stdscr.addstr(1, 1, 'Title', curses.A_BOLD)
    title_win = curses.newwin(1, sw-5, 3, 3)
    title_box = textpad.Textbox(title_win)
    textpad.rectangle(stdscr,2, 1, 4, sw-2)

    # Description
    stdscr.addstr(5, 1, 'Description', curses.A_BOLD)
    desc_win = curses.newwin(1, sw-5, 7, 3)
    desc_box = textpad.Textbox(desc_win)
    textpad.rectangle(stdscr,6, 1, 8, sw-2)

    # Priority 
    stdscr.addstr(9, 1, 'Priority', curses.A_BOLD)
    priority_win = curses.newwin(1, sw-5, 11, 3)
    priority_box = textpad.Textbox(priority_win)
    textpad.rectangle(stdscr,10, 1, 12, sw-2)

    # Due-Date 
    stdscr.addstr(13, 1, 'Due-Date', curses.A_BOLD)
    due_date_win = curses.newwin(1, sw-5, 15, 3)
    due_date_box = textpad.Textbox(due_date_win)
    textpad.rectangle(stdscr,14, 1, 16, sw-2)

    # add todo text
    add_todo_text = ' Add Todo'
    x_todo_text = (sw//2) - len(add_todo_text) // 2 
    stdscr.addstr(18, x_todo_text, add_todo_text, curses.A_BOLD)

    stdscr.refresh()
    curses.mousemask(1)

    title_text = ''
    desc_text = ''
    priority_text = ''
    due_date_text = ''
    while True:
        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            if y in range(2, 5) and x in range(sw-2):
                curses.curs_set(1)
                stdscr.attron(curses.color_pair(2))
                textpad.rectangle(stdscr,2, 1, 4, sw-2)
                stdscr.attroff(curses.color_pair(2))

                stdscr.refresh()
                title_box.edit()
                title_text = title_box.gather()
                curses.curs_set(0)

                stdscr.attron(curses.color_pair(4))
                textpad.rectangle(stdscr,2, 1, 4, sw-2)
                stdscr.addstr(3, 3, title_text)
                stdscr.attroff(curses.color_pair(4))
                stdscr.refresh()

            if y in range(6, 9) and x in range(sw-2):
                curses.curs_set(1)
                stdscr.attron(curses.color_pair(2))
                textpad.rectangle(stdscr,6, 1, 8, sw-2)
                stdscr.attroff(curses.color_pair(2))

                stdscr.refresh()
                desc_box.edit()
                desc_text = desc_box.gather()
                curses.curs_set(0)

                stdscr.attron(curses.color_pair(4))
                textpad.rectangle(stdscr,6, 1, 8, sw-2)
                stdscr.addstr(7, 3, desc_text)
                stdscr.attroff(curses.color_pair(4))
                stdscr.refresh()

            if y in range(10, 13) and x in range(sw-2):
                curses.curs_set(1)
                stdscr.attron(curses.color_pair(2))
                textpad.rectangle(stdscr,10, 1, 12, sw-2)
                stdscr.attroff(curses.color_pair(2))

                stdscr.refresh()
                priority_box.edit()
                priority_text = priority_box.gather()
                curses.curs_set(0)

                stdscr.attron(curses.color_pair(4))
                textpad.rectangle(stdscr,10, 1, 12, sw-2)
                stdscr.addstr(11, 3, priority_text)
                stdscr.attroff(curses.color_pair(4))
                stdscr.refresh()

            if y in range(14, 17) and x in range(sw-2):
                curses.curs_set(1)
                stdscr.attron(curses.color_pair(2))
                textpad.rectangle(stdscr,14, 1, 16, sw-2)
                stdscr.attroff(curses.color_pair(2))

                stdscr.refresh()
                due_date_box.edit()
                due_date_text = due_date_box.gather()
                curses.curs_set(0)

                stdscr.attron(curses.color_pair(4))
                textpad.rectangle(stdscr,14, 1, 16, sw-2)
                stdscr.addstr(15, 3, due_date_text)
                stdscr.attroff(curses.color_pair(4))
                stdscr.refresh()

            if y == 18:
                todo = Task(title_text, desc_text, priority_text, due_date_text)
                todo_list.append(todo)
                save_todo(todo_list)
                main(stdscr)



def remove_todo(stdscr):
    stdscr.clear()
    curses.curs_set(1)

    sh, sw = stdscr.getmaxyx()

    if sw > 50:
        sw = 50

    stdscr.addstr(0,1, 'Remove Todo', curses.A_BOLD)
    stdscr.addstr(2,1, 'Todo Index', curses.A_BOLD)
    delete_todo_win = curses.newwin(1, sw-5, 4, 3)
    delete_todo_box = textpad.Textbox(delete_todo_win)
    textpad.rectangle(stdscr,3, 1, 5, sw-2)
    stdscr.refresh()

    delete_todo_box.edit()
    index = int(delete_todo_box.gather()) - 1
    del todo_list[index]
    save_todo(todo_list)
    main(stdscr)


def bottom_nav(stdscr):
    sh, sw = stdscr.getmaxyx()
    x = 1
    y = sh

    a = 'a - add'
    e = 'e - edit'
    r = 'r - remove'
    q = 'q - quit'

    stdscr.addstr(y-2, x, a)
    stdscr.addstr(y-2, (sw-len(e))-1, e)
    stdscr.addstr(y-1, x, r)
    stdscr.addstr(y-1, (sw-len(e))-1, q)
    stdscr.refresh()


def main(stdscr):
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    print_title(stdscr)
    print_todo(stdscr)
    bottom_nav(stdscr)

    while True:
        key = stdscr.getkey()
        if key == 'q':
            break
        elif key == 'a':
            add_todo(stdscr)
        elif key == 'r':
            remove_todo(stdscr)


curses.wrapper(main)
