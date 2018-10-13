from task import Task
class Taskboard:
    def __init__(self):
        self.taskboard = []

    def new_task(self):
        task = Task()
        task.set_taskname(input("Task Name: "))
        task.set_taskdesc(input("Description: "))

        self.taskboard.append(task)

    def list_tasks(self):
        print("###################")
        print("Current Tasks:")
        print("###################")
        if len(self.taskboard) == 0:
            print("You don't have any tasks yet")
        else:
            for i in range(len(self.taskboard)):
                print(i)
            print("")

    def show_task(self):
        print("Type in Task Number")
        selection = input("> ")
        selection = int(selection)
        print("Task Name: %s" % self.taskboard[selection].taskname)