
import re

class Diary():
    # User-facing properties:
    #   entries: list of diary entries

    def __init__(self):
        self._entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of Diary_Entry
        # Side-effects:
        #   Adds the D.E to the entries property of the self object
        self._entries.append(entry)

    def search_for_diary_entry(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Diary Entry objects that have titles or content that includes the keyword
        # Side Effects:
        #   If keyword is * return all Diary Entries
        if self._entries == []:
            raise Exception("Warning! You have not added any diary entries")
        if keyword == "*":
            return self._entries
        else:
            return [entry for entry in self._entries if entry.read().lower().find(keyword.lower())!= -1]

    def pick_best_entry_to_read(self, minutes, wpm):
        # Parameters:
        #   minutes: integer, how much time the user has
        #   wpm : integer, how many words per minute can the user read
        # Returns:
        #   A list of Diary Entry objects that can be read within the given time
        # Side Effects:
        #   it will never give an entry that has more words that can be written in the given time
        if self._entries == []:
            raise Exception("Warning! You have not added any diary entries")
        readable_entries = []
        count_of_words_to_read = wpm * minutes
        words_read_so_far = 0
        while words_read_so_far < count_of_words_to_read:
            list_of_possible_entries = [entry for entry in self._entries 
                                        if entry.count_words() <= count_of_words_to_read and entry not in readable_entries]
            if list_of_possible_entries == []:
                return readable_entries
            list_of_word_count = [ entry.count_words() for entry in list_of_possible_entries]
            index = list_of_word_count.index(max(list_of_word_count))
            entry_to_read = list_of_possible_entries[index]
            readable_entries.append(entry_to_read)
            words_read_so_far += entry_to_read.count_words()
        return readable_entries

    def extract_contacts(self):
        # Returns:
        #   A list of all of the mobile phone numbers in the Diary object
        contacts = []
        if self._entries == []:
            raise Exception("Warning! You have not added any diary entries")
        for entry in self._entries:
            number = re.findall(r'\b0\d{10}', entry.read())
            contacts += number
        return contacts
    
        
        