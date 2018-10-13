class Task:
    #This is the class Constructor
    def __init__(self):
        self.taskname = ""
        self.taskdesc = ""

    # Class Method: set_taskname
    # INPUT: inName
    # EXPORT: None
    # Purpose: Set the name of the task
    def set_taskname(self,inName):
        self.taskname = inName

    # Class Method: set_taskdesc
    # INPUT: inDesc
    # EXPORT: None
    # Purpose: Set the description of the task
    def set_taskdesc(self,inDesc):
        self.taskdesc = inDesc

