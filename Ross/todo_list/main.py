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
    print("5. Edit Task")
    print("6. Save to Disk")
    print("7. Import from Disk")
    print("8. Exit")
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
        taskboard.edit_task()
    elif selected == 6:
        taskboard.save_data()
    elif selected == 7:
        taskboard.load_data()
    elif selected == 8:
        os._exit(0)