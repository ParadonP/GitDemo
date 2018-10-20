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
        ittr = 0
        print("#########################")
        print("Current Tasks:")
        print("#########################")
        if len(self.taskboard) == 0:
            print("You don't have any tasks yet")
        else:
            for i in (self.taskboard):
                print("%s. %s" % (ittr,i.get_taskname()))
                ittr += 1
        print("")

    def show_task(self):
        print("Type in Task Number")
        selection = input("> ")
        selection = int(selection)
        print("Task Name: %s" % self.taskboard[selection].taskname)
        print("Description:")
        print("%s" % self.taskboard[selection].get_taskdesc())

    def del_task(self):
        print("Type in Task Number to remove")
        selection = input("> ")
        selection = int(selection)
        print("Are you sure you want to remove Task: %s" % self.taskboard[selection].taskname)
        confirm = input("(y,n)> ")
        if confirm == "y":
            self.taskboard.pop(selection)
            print("Task successfully deleted")

    
