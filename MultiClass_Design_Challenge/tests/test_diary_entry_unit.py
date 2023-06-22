from lib.diary_entry import *
import pytest

'''
1)Trying to create an entry with no title
exception error "Warning! You need to give a title to your entry"
'''
def test_searching_no_title_entry():
    with pytest.raises(Exception) as e:
        day1 = Diary_Entry("", "Induction and Mac set-up")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need to give a title to your entry"

'''
2)Creating an entry with no content 
expeption error "Warning! You need to give some content to your entry"
'''
def test_searching_no_title_content():
    with pytest.raises(Exception) as e:
        day1 = Diary_Entry("Day 1 at Makers", "")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need to give some content to your entry"

'''
3)Creating an entry and counting words
Program returns 4
'''
def test_adding_entry_counitng_words():
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac setup")
    assert day1.count_words() == 4

'''
4)Creating an entry and read it
Program the format TITLE: CONTENT
'''
def test_reading_entry():
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac setup")
    assert day1.read() == "Day 1 at Makers: Induction and Mac setup"
