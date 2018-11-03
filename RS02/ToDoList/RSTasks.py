import json

class Task:
    # This is the class constructor
    def __init__(self):
        self.taskname = ""
        self.taskdesc = ""

        # Class Method: set_taskname
        # INPUT: inName
        # EXPORT: None
        # Purpose: Set the name of the task
    def set_taskname(self, inName):
            self.taskname = inName

        # Class Method: set_taskdesc
        # INPUT: inDesc
        # EXPORT: None
        # Purpose: Set the description of the task
    def set_taskdesc(self, inDesc):
            self.taskdesc = inDesc

    def get_taskname(self):
            return self.taskname

    def get_taskdesc(self):
            return self.taskdesc
        
    def export_json(self):
        output = json.dumps(self.__dict__)
        return output

