def sentence_verification(sentence):
    if sentence == "":
        raise Exception("Warning, no text given")
    capital_letter_check = sentence[0].isupper()
    ending_punctuation_check = any( char == sentence[-1] for char in [".", "!", "?"])
    return capital_letter_check and ending_punctuation_check
    
    