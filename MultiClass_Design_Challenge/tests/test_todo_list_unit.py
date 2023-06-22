from lib.todo_list import Todo_List
import pytest

#1) test empty list
def test_empty_list():
    empty_list = Todo_List()
    assert empty_list.show_todo() == []
    assert empty_list.show_complete() == []


#2) test empty list and try to update
#exception error "Warning! There is no such task"
def test_empty_list_cant_update():
    empty_list = Todo_List()
    with pytest.raises(Exception) as e:
        empty_list.update("walk the dog", "complete")
    err_msg = str(e.value)
    assert err_msg == "Warning! There is no such task in your list!"

#3) try to add a task with no description
#exception error "Warning! You need a description for the new task"
def test_cant_add_with_no_title():
    empty_list = Todo_List()
    with pytest.raises(Exception) as e:
        empty_list.add("")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need a description for the new task!"

'''
4) We add a task
we get the incomplete and complete list
'''
def test_adding_1task():
    new_list = Todo_List()
    new_list.add("Walk dog")
    assert new_list.show_todo() == [["Walk dog", "todo"]]
    assert new_list.show_complete() == []

'''
5) We add a task, complete a task
we get the incomplete and complete list
'''
def test_adding_and_completing_1task():
    new_list = Todo_List()
    new_list.add("walk dog")
    new_list.update("walk dog", "completed")
    assert new_list.show_todo() == []
    assert new_list.show_complete() == ["walk dog"]

'''
6) We add 2 tasks, complete 1
we get them in the incomplete
'''
def test_adding_2tasks_complete1():
    new_list = Todo_List()
    new_list.add("walk dog")
    new_list.add("walk cat")
    new_list.update("walk dog", "completed")
    new_list.update("walk cat", "in progress")
    assert new_list.show_todo() == [["walk cat", "in progress"]]
    assert new_list.show_complete() == ["walk dog"]

'''
7) We add 4 tasks, complete 2
we get them in the incomplete and todo
'''
def test_adding_4tasks_complete2():
    new_list = Todo_List()
    new_list.add("walk dog")
    new_list.add("walk cat")
    new_list.add("walk fish")
    new_list.add("walk Jack")
    new_list.update("walk dog", "completed")
    new_list.update("walk cat", "in progress")
    new_list.update("walk Jack", "completed")
    assert new_list.show_todo() == [["walk cat", "in progress"], ["walk fish", "todo"]]
    assert new_list.show_complete() == ["walk dog", "walk Jack"]