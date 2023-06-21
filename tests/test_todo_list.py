from lib.todo import *
from lib.todo_list import *

#test empty list
def test_empty_list():
    empty_list = TodoList()
    assert empty_list.incomplete() == []
    assert empty_list.complete() == []


#test empty list and give up
def test_empty_and_give_up():
    empty_list = TodoList()
    empty_list.give_up()
    assert empty_list.incomplete() == []
    assert empty_list.complete() == []

'''
We add a task
we get the incomplete and complete list
'''
def test_adding_1task():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    assert new_list.incomplete() == [task1]
    assert new_list.complete() == []

'''
We add a task, complete a task
we get the incomplete and complete list
'''
def test_adding_and_completing_1task():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task1.mark_complete()
    assert new_list.incomplete() == []
    assert new_list.complete() == [task1]

'''
We add 3 tasks
we get the incomplete and complete list
'''
def test_adding_3tasks():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task2 = Todo("Walk cat")
    new_list.add(task2)
    task3 = Todo("Walk fish")
    new_list.add(task3)
    assert new_list.incomplete() == [task1, task2, task3]
    assert new_list.complete() == []

'''
We add 3 tasks, complete 1 task
we get the incomplete and complete list
'''
def test_adding_3tasks_and_complete_1():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task2 = Todo("Walk cat")
    new_list.add(task2)
    task3 = Todo("Walk fish")
    new_list.add(task3)
    task2.mark_complete()
    assert new_list.incomplete() == [task1, task3]
    assert new_list.complete() == [task2]

'''
We add 3 tasks, give up
we get the incomplete and complete list
'''
def test_adding_3tasks_and_give_up():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task2 = Todo("Walk cat")
    new_list.add(task2)
    task3 = Todo("Walk fish")
    new_list.add(task3)
    new_list.give_up()
    assert new_list.incomplete() == []
    assert new_list.complete() == [task1, task2, task3]

'''
We add 3 tasks, complete2
we get the incomplete and complete list
'''
def test_adding_3tasks_and_complete_2():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task2 = Todo("Walk cat")
    new_list.add(task2)
    task3 = Todo("Walk fish")
    new_list.add(task3)
    task3.mark_complete()
    task1.mark_complete()
    assert new_list.incomplete() == [task2]
    assert new_list.complete() == [task1, task3]

'''
We add 3 tasks, complete, give up
we get the incomplete and complete list
'''
def test_adding_3tasks_and_complete1_and_giveup():
    new_list = TodoList()
    task1 = Todo("Walk dog")
    new_list.add(task1)
    task2 = Todo("Walk cat")
    new_list.add(task2)
    task3 = Todo("Walk fish")
    new_list.add(task3)
    task3.mark_complete()
    assert new_list.incomplete() == [task1, task2]
    assert new_list.complete() == [task3]
    new_list.give_up()
    assert new_list.incomplete() == []
    assert new_list.complete() == [task1, task2, task3]