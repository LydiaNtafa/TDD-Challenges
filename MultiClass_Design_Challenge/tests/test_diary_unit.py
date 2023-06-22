from lib.dairy import Diary
import pytest

'''
1)When no Diary Entries added and try to search *,
expeption error "Warning! You have not added any diary entries"
'''
def test_searching_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_diary.search_for_diary_entry("*")
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"

'''
2)When no Diary Entries added and try to search for best entry to read,
expeption error "Warning! You have not added any diary entries"
'''
def test_pick_best_entry_to_read_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_diary.pick_best_entry_to_read(2, 50)
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"

'''
3)When no Diary Entries added and try to get a list of all the phone numbers
expeption error "Warning! You have not added any diary entries"
'''
def test_extract_numbers_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_diary.extract_contacts()
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"