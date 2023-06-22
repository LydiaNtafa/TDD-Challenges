class Diary_Entry():

    def __init__(self, title, content):
        if title == "":
            raise Exception("Warning! You need to give a title to your entry")
        if content =="":
            raise Exception("Warning! You need to give some content to your entry")
        self._title = title 
        self._contents = content


    def count_words(self):
        # Returns:
        #   Integer : count of words in contents
        return len(self._contents.split())

    def read(self):
        # Returns:
        #   string : TITLE: CONTENT
        return f"{self._title}: {self._contents}"