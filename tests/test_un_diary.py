from lib.diary import *

'''
Initially empty diary
'''
def test_empty_diary():
    dear_diary = Diary()
    assert dear_diary.all() == []



