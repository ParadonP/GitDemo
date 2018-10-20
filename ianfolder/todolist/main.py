from taskboard import Taskboard
import os

taskboard = Taskboard()

def show_menu():
    print("#########################")
    print("Taskboard Menu")
    print("#########################")
    print("Type a number to continue")
    print("1. add Task")
    print("2. list Tasks")
    print("3. Show Task")
    print("4. Delete Task")
    print("5. Exit")
    selection = input("> ")
    selection = int(selection)

    return selection

while True:
    selected = show_menu()
    if selected == 1:
        taskboard.new_task()
    elif selected == 2:
        taskboard.list_tasks()
    elif selected == 3:
        taskboard.show_task()
    elif selected == 4:
        taskboard.del_task()
    elif selected == 5:
        os._exit(0)