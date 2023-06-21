from lib.diary_entry import DiaryEntry
from lib.diary import Diary

'''
When we add 2 diary entries
We get the entries back in a list 
'''
def test_2diary_entries_and_display():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", "Induction and laptop set up")
    day2 = DiaryEntry("Day 2", "Learning the command line")
    makers_diary.add(day1)
    makers_diary.add(day2)
    assert makers_diary.all() == [day1, day2]

'''
When we add 2 diary entries
We get the number of words in the diary's context
'''
def test_coutning_words_for_2_entries():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", "Induction and laptop set up")
    day2 = DiaryEntry("Day 2", "Learning the command line")
    makers_diary.add(day1)
    makers_diary.add(day2)
    assert makers_diary.count_words() == 9

'''
When we add 2 diary entries
We count the reading time for wmp = 2
'''
def test_reading_time_for_2_entries():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", "Induction and laptop set up")
    day2 = DiaryEntry("Day 2", "Learning the command line")
    makers_diary.add(day1)
    makers_diary.add(day2)
    assert makers_diary.reading_time(2) == 4

    '''
When we add 2 big diary entries
We find the best entry for reading time 1 minute and wmp = 50
'''
def test_best_entry_for_1minute_reading_time():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,50)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    assert makers_diary.find_best_entry_for_reading_time(50, 1) == day2

    '''
When we add 4 diary entries
We get none for not too much time to read anything
'''
def test_best_entry_for_tooshort_time():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,50)))
    day3 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,24)))
    day4 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.find_best_entry_for_reading_time(2, 4) == None

    '''
When we add 4 diary entries
We find the best entry for reading time 2 minute and wmp = 37
'''
def test_best_entry_for_2minute_reading_time():
    makers_diary = Diary()
    day1 = DiaryEntry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,50)))
    day3 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,24)))
    day4 = DiaryEntry("Day 2", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.find_best_entry_for_reading_time(37, 2) == day2