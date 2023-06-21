from lib.diary_entry1 import *

my_diary = DiaryEntry("My goal for Makers", "I want to make friends")
empty_diary = DiaryEntry("", "")
wpm = 200

def test_format():
    assert my_diary.format() == "My goal for Makers: I want to make friends"
    

def test_count_given_empty_string():
    assert empty_diary.count_words() == 0


def test_count_given_my_diary():
    assert my_diary.count_words() == 5
    
def test_reading_time_for_empty_string():
    assert empty_diary.reading_time(wpm) == "No words given"
    
def test_reading_time_with_big_diary_given():
    big_diary = DiaryEntry("These are 500 words", " ".join([f'word{i}' for i in range(0, 500)]))
    assert big_diary.reading_time(wpm) == f"It will take you approximately 2 min/s to read this"

def test_reading_chunk_for_empty_diary():
    assert empty_diary.reading_chunk(wpm, 1) == ""

    
def test_reading_chunk_for_big_diary_restart():
    big_diary = DiaryEntry("These are 500 words", " ".join([f'word{i}' for i in range(0, 500)]))
    assert big_diary.reading_chunk(100, 1) == " ".join([f'word{i}' for i in range(0, 100)])
    assert big_diary.reading_chunk(100, 2) == " ".join([f'word{i}' for i in range(100, 300)])
    assert big_diary.reading_chunk(wpm, 2) == " ".join([f'word{i}' for i in range(300, 500)])
    assert big_diary.reading_chunk(100, 1) == " ".join([f'word{i}' for i in range(0, 100)])
    assert big_diary.reading_chunk(100, 1) == " ".join([f'word{i}' for i in range(100, 200)])
