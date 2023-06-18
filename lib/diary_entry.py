class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        self.bookmark = 0
    
    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if self.count_words() == 0:
            return "No words given" 
        else:
            words_calculation = round(self.count_words() / wpm)
            return f"It will take you approximately {words_calculation} min/s to read this"
        

    def reading_chunk(self, wpm, minutes):
        count_of_words_to_read = wpm * minutes
        list_of_words = self.contents.split()
        slice_list = list_of_words[self.bookmark:(count_of_words_to_read+self.bookmark)]
        new_string = " ".join(slice_list)
        if self.bookmark+count_of_words_to_read >= self.count_words():
            self.bookmark = 0
        else:
            self.bookmark += count_of_words_to_read
        return new_string
    
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.