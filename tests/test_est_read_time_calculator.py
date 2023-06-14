from lib.est_read_time_calculator import *

'''
If we give an empty string
it will return 0 mins"
'''
def test_empty_string():
    assert estimate_reading_time("") == "This text will take you less than a minute to read"

'''
If we give a text of 99 words
it will return 0 mins"
'''
def test_99words_text():
    text = " ".join(['word' for i in range(0, 99)])
    assert estimate_reading_time(text) == "This text will take you less than a minute to read"

'''
If we give a text of 100 words
it will return 1 min"
'''
def test_100words_text():
    text = " ".join(['word' for i in range(0, 100)])
    assert estimate_reading_time(text) == "This text will take you approximately 1 minute to read"

'''
If we give a text of 500 words
it will return 3 mins"
'''
def test_500words_text():
    text = " ".join(['word' for i in range(0, 500)])
    assert estimate_reading_time(text) == "This text will take you approximately 2 minutes to read"

'''
If we give a text of 1224 words
it will return 1 hour"
'''
def test_12000words_text():
    text = " ".join(['word' for i in range(0, 12000)])
    assert estimate_reading_time(text) == "This text will take you approximately 1 hour to read"

'''
If we give a text of 36000 words
it will return 1 hour"
'''
def test_36000words_text():
    text = " ".join(['word' for i in range(0, 36000)])
    assert estimate_reading_time(text) == "This text will take you approximately 3.0 hours to read"