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
        tasksfound = False
        ittr = 0
        print("#########################")
        print("Current Tasks:")
        print("#########################")
        if len(self.taskboard) == 0:
            print("You don't have any tasks yet")
        else:
            tasksfound = True
            for i in (self.taskboard):
                print("%s. %s" % (ittr,i.get_taskname()))
                ittr += 1
        print("")
        return tasksfound

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
        if confirm == "y" or confirm == "Y":
            self.taskboard.pop(selection)
            print("Task successfully deleted")
        elif confirm == "n" or confirm == "N":
            print("Task not deleted")
        else:
            print("Unknown input")

    def edit_task(self):
        if self.list_tasks():
            print("What task do you want to edit?")
            selection = input("> ")
            selection = int(selection)
            #This show the detail of the sellected task
            print("Task Name: %s" % self.taskboard[selection].taskname)
            print("Description:")
            print("%s" % self.taskboard[selection].get_taskdesc())
            #This will prompt for a new task name and new description
            self.taskboard[selection].set_taskname(input("New Task Name: "))
            self.taskboard[selection].set_taskdesc(input("New Description: "))
    


    
