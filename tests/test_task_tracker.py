import pytest
from lib.task_tracker import *

# Test for empty string as an argument
def test_empty_string():
    assert task_tracker("") == "Warning! Empty text was entered!"

# Test for a number as an argument
def test_for_non_string_agrument_given():
    with pytest.raises(Exception) as e:
        task_tracker(19) 
    err_msg = str(e.value)
    assert err_msg == "Warning! No text was entered!"

# Test a text that includes the key string_with_special_character:
def test_for_text_that_includes_the_key_string_with_colon():
    assert task_tracker("#TODO: Walk the dog!") == True

# Test a text that includes the key string_by_itself:
def test_for_text_that_includes_the_key_string():
    assert task_tracker("This is a #TODO list!") == True

# Test a text without the key string 
def test_for_text_without_key_string():
    assert task_tracker("This is a to-do list") == False

# Test a text with #todo
def test_for_text_that_includes_key_string_lowercase():
    assert task_tracker("This is a #todo list!") == False

# Test a text with #Todo
def test_for_text_that_includes_key_string_capitalise():
    assert task_tracker("This is a #Todo list!") == False

# Test an uppercase text with key string
def test_for_uppercase_text_that_includes_key_string():
    assert task_tracker("THIS IS A #TODO LIST!") == True

# Test an uppercase text with key string without hash
def test_for_uppercase_text_that_includes_key_string_without_hash():
    assert task_tracker("THIS IS A TODO LIST!") == False

# Test a text with key string replacing hash with :
def test_for_uppercase_text_that_includes_key_string_replacing_special_character():
    assert task_tracker("This is a :TODO list!") == False

# Test a text with key string replacing Os for 0s:
def test_for_uppercase_text_that_includes_key_string_replacing_Os_for_0s():
    assert task_tracker("This is a #T0D0 list!") == False