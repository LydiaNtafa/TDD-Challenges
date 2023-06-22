from lib.dairy import Diary
from lib.diary_entry import Diary_Entry
import pytest

'''
1)When adding multiple Diary Entries and try to search for no match
Program comes back with empty list
'''
def test_searching_for_python():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up")
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.")
    dear_diary.add(day1)
    dear_diary.add(day2)
    assert dear_diary.search_for_diary_entry("python") == []

'''
2)When adding multiple Diary Entries and try to search *,
They come back as a list of entries
'''
def test_searching_for_all_multiple_entries():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up")
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.")
    dear_diary.add(day1)
    dear_diary.add(day2)
    assert dear_diary.search_for_diary_entry("*") == [day1, day2]

'''
3)When adding multiple Diary Entries and try to search for whole of title,
Program comes back with that entry
'''
def test_searching_for_day_2_at_Makers():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up")
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.")
    dear_diary.add(day1)
    dear_diary.add(day2)
    assert dear_diary.search_for_diary_entry("Day 2 at Makers") == [day2]

'''
4)When adding multiple Diary Entries and try to search for part of content,
Program comes back with that entry
'''
def test_searching_for_mac():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up")
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.")
    dear_diary.add(day1)
    dear_diary.add(day2)
    assert dear_diary.search_for_diary_entry("mac") == [day1]

'''
5)When we add 2 big diary entries
We find the best entry for reading time 1 minute and wmp = 50
'''
def test_best_entry_for_1minute_reading_time():
    makers_diary = Diary()
    day1 = Diary_Entry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,50)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    assert makers_diary.pick_best_entry_to_read(1, 50) == [day2]

'''
6)When we add 4 diary entries
We get none for not too much time to read anything
'''
def test_best_entry_for_tooshort_time():
    makers_diary = Diary()
    day1 = Diary_Entry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,50)))
    day3 = Diary_Entry("Day 3", " ".join( "word" for i in range(0,24)))
    day4 = Diary_Entry("Day 4", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.pick_best_entry_to_read(2, 4) == []

'''
7)When we add 4 diary entries
We find the best entry for reading time 2 minute and wmp = 45
'''
def test_best_entry_for_2minute_reading_time():
    makers_diary = Diary()
    day1 = Diary_Entry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,30)))
    day3 = Diary_Entry("Day 3", " ".join( "word" for i in range(0,50)))
    day4 = Diary_Entry("Day 4", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.pick_best_entry_to_read(2, 45) == [day3, day2]

'''
8)When adding multiple Diary Entries with no mobile number and try to extract contacts,
Program comes back with that entry
'''
def test_searching_for_contacts_where_no_contacts():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up")
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.")
    dear_diary.add(day1)
    dear_diary.add(day2)
    assert dear_diary.extract_contacts() == []

'''
9)When adding a Diary Entry with a mobile number and try to extract contacts,
Program comes back with that number
'''
def test_searching_for_contacts_where_1_contact():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    assert dear_diary.extract_contacts() == ["07978532579"]

'''
10_When adding mutiple Diary Entries with some mobile numbers and try to extract contacts,
Program comes back with a list of numbers
'''
def test_searching_for_contacts_where_2_contacts_and_1random_number():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.This is not a phone number 12345678901 and neither is this 03456789")
    dear_diary.add(day2)
    day3 = Diary_Entry("Day 3", "Another phone number is 07930000330")
    dear_diary.add(day3)
    assert dear_diary.extract_contacts() == ["07978532579","07930000330"]

'''
11)When adding mutiple Diary Entries with some mobile numbers and try to read that entry,
Program comes back with the TITLE: CONTENT
'''
def test_reading_the_entry_that_containts_the_first_contact():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.This is not a phone number 12345678901 and neither is this 03456789")
    dear_diary.add(day2)
    day3 = Diary_Entry("Day 3", "Another phone number is 07930000330")
    dear_diary.add(day3)
    assert dear_diary.search_for_diary_entry(dear_diary.extract_contacts()[0])[0].read() == "Day 1 at Makers: Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text"