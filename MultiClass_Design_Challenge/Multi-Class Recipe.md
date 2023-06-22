{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. 
The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

┌────────────────────────────┐      ┌────────────────────────────┐
│ Diary                      │      │ Todo list                  │
│                            │      │                            │    
│ - add(D.E)                 │      │ - Add(task, status)        │
│ - search_D.E(keyword)      │      │ - update(task,status)      │
│ - to_read_D.E(min,wpm)     │      │ - show_todo()              │
│   => one or more D.E       │      │ - show_complete()          │
│ - extract_contacts()       │      └────────────────────────────┘
│    => list_of_cntcts       │      
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────────┐      
│ Diary Entry(title, content) │      
│                             │     
│ - count_words()             │      
│ - read()                    │               
└─────────────────────────────┘
Also design the interface of each class in more detail.

class Diary():
    # User-facing properties:
    #   entries: list of diary entries

    def __init__(self):
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of Diary_Entry
        # Side-effects:
        #   Adds the D.E to the entries property of the self object
        pass # No code here yet

    def search_for_diary_entry(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Diary Entry objects that have titles or content that includes the keyword
        # Side Effects:
        #   If keyword is * return all Diary Entries
        pass # No code here yet

    def pick_best_entry_to_read(self, minutes, wpm):
        # Parameters:
        #   minutes: integer, how much time the user has
        #   wpm : integer, how many words per minute can the user read
        # Returns:
        #   A list of Diary Entry objects that can be read within the given time
        # Side Effects:
        #   it will never give an entry that has more words that can be written in the given time
        pass # No code here yet

    def extract_contacts(self):
        # Returns:
        #   A list of all of the mobile phone numbers in the Diary object
        pass # No code here yet


class Diary_Entry():
    # Public properties:
    #   title: string
    #   content: string

    def __init__(self, title, content):
        # Parameters:
        #   title: string
        #   content: string
        # Side-effects:
        #   Sets the title and content properties
        pass # No code here yet

    def count_words(self):
        # Returns:
        #   Integer : count of words in contents

    def read(self):
        # Returns:
        #   string : TITLE: CONTENT


class Todo_List():

    def __init__(self):
        #   Creates a new list
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets the status to "todo" and add the task to the list
        pass

    def update(task, status):
        # Parameters:
        #   task: string
        #   status : string
        # Side-effects:
        #   Updates the status of the given task
        pass
      
    def show_todo(self):
        # Returns:
        #   A list of incomplete tasks with their status
        pass

    def show_complete(self):
        # Returns:
        #   A list of completed tasks
        pass


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
'''
When adding multiple Diary Entries and try to search for no match
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
When adding multiple Diary Entries and try to search *,
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
When adding multiple Diary Entries and try to search for whole of title,
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
When adding multiple Diary Entries and try to search for part of content,
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
When we add 2 big diary entries
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
When we add 4 diary entries
We get none for not too much time to read anything
'''
def test_best_entry_for_tooshort_time():
    makers_diary = Diary()
    day1 = Diary_Entry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,50)))
    day3 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,24)))
    day4 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.makers_diary.pick_best_entry_to_read(2, 4) == []

'''
When we add 4 diary entries
We find the best entry for reading time 2 minute and wmp = 45
'''
def test_best_entry_for_2minute_reading_time():
    makers_diary = Diary()
    day1 = Diary_Entry("Day 1", " ".join( "word" for i in range(0,100)))
    day2 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,30)))
    day3 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,50)))
    day4 = Diary_Entry("Day 2", " ".join( "word" for i in range(0,130)))
    makers_diary.add(day1)
    makers_diary.add(day2)
    makers_diary.add(day3)
    makers_diary.add(day4)
    assert makers_diary.makers_diary.pick_best_entry_to_read(2, 45) == [day3, day2]

'''
When adding multiple Diary Entries with no mobile number and try to extract contacts,
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
When adding a Diary Entry with a mobile number and try to extract contacts,
Program comes back with that number
'''
def test_searching_for_contacts_where_no_contacts():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    assert dear_diary.extract_contacts() == ["07978532579"]

'''
When adding mutiple Diary Entries with some mobile numbers and try to extract contacts,
Program comes back with a list of numbers
'''
def test_searching_for_contacts_where_no_contacts():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.This is not a phone number 12345678901 and neither is this 03456789")
    dear_diary.add(day2)
    day3 = Diary_Entry("Day 3", "Another phone number is 07930000330")
    dear_diary.add(day3)
    assert dear_diary.extract_contacts() == ["07978532579","07930000330"]

'''
When adding mutiple Diary Entries with some mobile numbers and try to read that entry,
Program comes back with the TITLE: CONTENT
'''
def test_searching_for_contacts_where_no_contacts():
    dear_diary = Diary()
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text")
    dear_diary.add(day1)
    day2 = Diary_Entry("Day 2 at Makers", "Learning about the command line.This is not a phone number 12345678901 and neither is this 03456789")
    dear_diary.add(day2)
    day3 = Diary_Entry("Day 3", "Another phone number is 07930000330")
    dear_diary.add(day3)
    assert search_for_diary_entry(dear_diary.extract_contacts()[0])[0].read() == "Day 1 at Makers: nduction and Mac set-up. I also met Sarah today and she gave me her number 07978532579! I need to remember to send her a text"

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

# Diary unit tests
'''
When no Diary Entries added and try to search *,
expeption error "Warning! You have not added any diary entries"
'''
def test_searching_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_diary.search_for_diary_entry("*")
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"

'''
When no Diary Entries added and try to search for best entry to read,
expeption error "Warning! You have not added any diary entries"
'''
def test_pick_best_entry_to_read_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_diary.pick_best_entry_to_read(2, 50)
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"

'''
When no Diary Entries added and try to get a list of all the phone numbers
expeption error "Warning! You have not added any diary entries"
'''
def test_pick_best_entry_to_read_in_empty_diary():
    dear_diary = Diary()
    with pytest.raises(Exception) as e:
        dear_extract contacts
    err_msg = str(e.value)
    assert err_msg == "Warning! You have not added any diary entries"

# Diary Entry unit tests
'''
Trying to create an entry with no title
exception error "Warning! You need to give a title to your entry"
'''
def test_searching_no_title_entry():
    with pytest.raises(Exception) as e:
        day1 = Diary_Entry("", "Induction and Mac set-up")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need to give a title to your entry"

'''
Creating an entry with no content 
expeption error "Warning! You need to give some content to your entry"
'''
def test_searching_no_title_content():
    with pytest.raises(Exception) as e:
        day1 = Diary_Entry("Day 1 at Makers", "")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need to give some content to your entry"

'''
Creating an entry and counting words
Program returns 4
'''
def test_searching_no_title_content():
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac setup")
    assert day1.count_words() == 4

'''
Creating an entry and read it
Program the format TITLE: CONTENT
'''
def test_searching_no_title_content():
    day1 = Diary_Entry("Day 1 at Makers", "Induction and Mac setup")
    assert day1.read() == "Day 1 at Makers: Innduction and Mac setup"

# Todo List unit tests
#test empty list
def test_empty_list():
    empty_list = TodoList()
    assert empty_list.show_todo() == []
    assert empty_list.show_complete() == []


#test empty list and try to update
#exception error "Warning! There is no such task"
def test_empty_list_cant_update():
    empty_list = TodoList()
    with pytest.raises(Exception) as e:
        empty_list.update("walk the dog", "complete")
    err_msg = str(e.value)
    assert err_msg == "Warning! There is no such task in your list!"

#try to add a task with no description
#exception error "Warning! You need a description for the new task"
def test_cant_add_with_no_title():
    empty_list = TodoList()
    with pytest.raises(Exception) as e:
        empty_list.add("")
    err_msg = str(e.value)
    assert err_msg == "Warning! You need a description for the new task!"

'''
We add a task
we get the incomplete and complete list
'''
def test_adding_1task():
    new_list = TodoList()
    new_list.add("Walk dog")
    assert new_list.show_todo() == [["Walk dog", "todo"]]
    assert new_list.show_complete() == []

'''
We add a task, complete a task
we get the incomplete and complete list
'''
def test_adding_and_completing_1task():
    new_list = TodoList()
    new_list.add("Walk dog")
    new_list.update("walk the dog", "completed")
    assert new_list.show_todo() == []
    assert new_list.show_complete() == ["walk the dog"]

'''
We add 2 tasks, complete 1
we get them in the incomplete
'''
def test_adding_3tasks():
    new_list = TodoList()
    new_list.add("Walk dog")
    new_list.add("Walk cat")
    new_list.update("walk dog", "completed")
    new_list.update("walk cat", "in progress")
    assert empty_list.show_todo() == ["walk cat", "in progress"]
    assert empty_list.show_complete() == ["walk dog"]


5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.