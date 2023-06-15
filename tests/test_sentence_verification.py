from lib.sentence_verification import *
import pytest

def test_empty_string():
    with pytest.raises(Exception) as e:
        sentence_verification("")
    err_msg = str(e.value)
    assert err_msg == "Warning, no text given"

def test_one_word_with_exclamation():
    assert sentence_verification("Hello!")

def test_one_word():
    assert not sentence_verification("Hello")

def test_valid_sentence():
    assert sentence_verification("Hello World, it's me!")

def test_lower_case_word():
    assert not sentence_verification("lol!")