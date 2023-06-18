class GrammarStats:
    def __init__(self):
        self.checked_texts = 0
        self.passed_texts = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.checked_texts += 1
        if text == "":
            raise Exception("Warning, no text given")
        capital_letter_check = text[0].isupper()
        ending_punctuation_check = text[-1] in ".!?"
        if capital_letter_check and ending_punctuation_check:
            self.passed_texts += 1
            return True
        else:
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
         return round((self.passed_texts * 100)/self.checked_texts)