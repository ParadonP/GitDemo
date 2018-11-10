from RSTasks import Task
import json

class Taskboard:
    def __init__(self):
        self.taskboard = []

    def new_task(self):
        task = Task()
        task.set_taskname(input("Task Name: "))
        task.set_taskdesc(input("Description: "))

        self.taskboard.append(task)

    def list_tasks(self):
        taskfound = False
        ittr = 0
        print("#########################")
        print("Current Tasks:")
        print("#########################")
        if len(self.taskboard) == 0:
            print("You don't have any tasks yet")
        else:
            taskfound = True
            for i in (self.taskboard):
                print("%s. %s" % (ittr,i.get_taskname()))
                ittr += 1
        print("")
        return taskfound

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
            print("Task no deleted")
        else:
            print("Unknown input")
        
    def edit_task(self):
        if self.list_tasks():
            print("What Task do you want to edit?")
            selection = input("> ")
            selection = int(selection)
            #This shows the details of the selected task.
            print("Task Name: %s" % self.taskboard[selection].taskname)
            print("Description:")
            print("%s" % self.taskboard[selection].get_taskdesc())
            #This will prompt for a new task name and new description.
            self.taskboard[selection].set_taskname(input("New Task Name: "))
            self.taskboard[selection].set_taskdesc(input("New Description: "))

    def save_data(self):
        tmp = []
        # Loop through all the tasks
        for t in self.taskboard:
            tmp.append(t.export_dict())
        # Write to file
        try:
            with open('data.json', 'w') as fp:
                json.dump(tmp, fp, indent=4)
            print("Save Successful")  
        except:
            print("Didn't save correctly")

    def load_data(self):
        try:
            with open('data.json') as json_file:
                data = json.load(json_file)

            # Create Task Object, load in dictionary into object.
            for d in data:
                task = Task()
                task.set_taskname(d['Name'])
                task.set_taskdesc(d['Description'])
                self.taskboard.append(task)
            print("Load Successful")  
        except:
            print("Didn't load correctly")
