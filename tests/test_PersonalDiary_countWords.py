from lib.PersonalDiary import *

'''
Given empty string
returns 0
'''
def test_given_empty_string():
    result = count_words("")
    assert result == 0

'''
Given 4word string
returns 4
'''
def test_given_4word_string():
    result = count_words("This is not 5words")
    assert result == 4

'''
Given 1word string
returns 1
'''
def test_given_1word_string():
    result = count_words("Test")
    assert result == 1