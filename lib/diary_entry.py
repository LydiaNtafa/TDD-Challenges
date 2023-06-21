class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title 
        self.contents = contents
        self._bookmark = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if self.count_words() == 0:
            return "No words given" 
        else:
            words_calculation = round(self.count_words() / wpm)
            return f"It will take you approximately {words_calculation} min/s to read this"

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        count_of_words_to_read = wpm * minutes
        list_of_words = self.contents.split()
        slice_list = list_of_words[self._bookmark:(count_of_words_to_read+self._bookmark)]
        new_string = " ".join(slice_list)
        if self._bookmark+count_of_words_to_read >= self.count_words():
            self._bookmark = 0
        else:
            self._bookmark += count_of_words_to_read
        return new_string