class Todo_List():

    def __init__(self):
        #   Creates a new list
        self.todo = []

    def add(self, task):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets the status to "todo" and add the task to the list
        if task == "":
            raise Exception("Warning! You need a description for the new task!")
        self.todo.append([task, "todo"])

    def update(self,task, status):
        # Parameters:
        #   task: string
        #   status : string
        # Side-effects:
        #   Updates the status of the given task

        if self.todo == [] or any(task in sublist for sublist in self.todo) == False:
            raise Exception("Warning! There is no such task in your list!")
        else:
            for i in range(len(self.todo)):
                if self.todo[i][0] == task:
                    self.todo[i][1] = status
        

    def show_todo(self):
        # Returns:
        #   A list of incomplete tasks with their status
        return [task for task in self.todo if task[1]!="completed"]
    
    def show_complete(self):
        # Returns:
        #   A list of completed tasks
        return [task[0] for task in self.todo if task[1]=="completed"]
