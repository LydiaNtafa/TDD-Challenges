from lib.PersonalDiary import *
import pytest

"""
Given string is empty
It returns the string
"""
def test_given_is_empty():
    result = make_snipet("")
    assert result == ""

"""
Given string is less than 5 words
It returns the string
"""
def test_given_less_than_5_words():
    result = make_snipet("This is not 5words")
    assert result == "This is not 5words"

'''
Given string is more than 5 words
It returns the 5 first words and then "..."
'''
def test_given_more_than_5_words():
    result = make_snipet("This is more than words now for sure")
    assert result == "This is more than words..."

'''
Given entry is not a string
Return Exception Error
'''
def test_given_is_not_a_string():
    with pytest.raises(Exception) as e:
        make_snipet(666.99)
    err_msg = str(e.value)
    assert err_msg == "Invalid Input, please enter text!!!"
