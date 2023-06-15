def task_tracker(text):
    if type(text) is not str:
        raise Exception ("Warning! No text was entered!")
    
    if text == "":
        return "Warning! Empty text was entered!"
    else:
        return text.find("#TODO") != -1
