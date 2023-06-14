def count_words(text):
    list_of_text = text.split()
    return len(list_of_text)


def make_snipet(text):
    if type(text) is not str:
        raise Exception("Invalid Input, please enter text!!!")
    
    if count_words(text) < 5:
        return text
    
    list_of_text = text.split()
    list_of_5_words_max = list_of_text[:5]
    list_of_5_words_max[-1] += "..."
    snipet = " ".join(list_of_5_words_max)
    return snipet
