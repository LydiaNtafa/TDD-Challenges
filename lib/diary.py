class Diary:
    def __init__(self):
        pass
        self._entries_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._entries_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._entries_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum([entry.count_words() for entry in self._entries_list])


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return round(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        count_of_words_to_read = wpm * minutes
        list_of_possible_entries = [entry for entry in self._entries_list 
                                    if entry.count_words() <= count_of_words_to_read]
        if list_of_possible_entries == []:
            return None
        list_of_word_count = [ entry.count_words() for entry in list_of_possible_entries]
        index = list_of_word_count.index(max(list_of_word_count))
        
        return list_of_possible_entries[index]
