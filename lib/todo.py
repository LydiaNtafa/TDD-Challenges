class Todo:

    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True