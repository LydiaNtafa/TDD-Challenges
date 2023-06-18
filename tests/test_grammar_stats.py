from lib.Grammar_Stats import *
import pytest


def test_empty_string():
    new_obj = GrammarStats()
    with pytest.raises(Exception) as e:
        new_obj.check("")
    err_msg = str(e.value)
    assert err_msg == "Warning, no text given"
    assert new_obj.check("Hello!")
    assert not new_obj.check("Hello")
    assert new_obj.percentage_good() == 33
    assert new_obj.check("Hello World, it's me!")
    assert new_obj.percentage_good() == 50
    assert not new_obj.check("lol!")
    assert new_obj.check("Hello World, it's me!")
    assert new_obj.percentage_good() == 50