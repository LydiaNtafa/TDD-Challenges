# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todos_list = []

    def add(self, todo):
        self._todos_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [task for task in self._todos_list if task.complete == False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [task for task in self._todos_list if task.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self._todos_list:
            task.complete = True


