def estimate_reading_time(text):
    word_count = text.count(" ") + 1
    if word_count < 100:
        return "This text will take you less than a minute to read"
    elif word_count < 300:
        return "This text will take you approximately 1 minute to read"
    elif word_count < 10000:
        '''
        if it takes more than 1 minute and less than 50 minutes
        the resuld is given out in x minutes (rounded integer)
        '''
        minutes = round(word_count/200)
        return f"This text will take you approximately {minutes} minutes to read"
    elif word_count < 12800:
        '''
        if it takes more than 50 minutes and less than 64 minutes
        the result is about an hour
        '''
        return "This text will take you approximately 1 hour to read"
    else:
        '''
        if it takes more than 64 minutes
        the resuld is given out in x hours (rounded to 1 decimal)
        '''
        hours = round (word_count/12000, 1) 
        return f"This text will take you approximately {hours} hours to read"

    