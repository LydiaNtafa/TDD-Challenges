# Function Design Recipe

## 1. Describe the Problem
*Put or write the user story here. Add any clarifying notes you might have.*

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

## 2. Design the Function Signature
*Include the name of the function, its parameters, return value, and side effects.*

**Name, arguments, return value** : 
def task_tracker(text):
    return boolean

**Funcitonality**: 
Checks if a text includes the "#TODO"

**Side effects**: 


## 3. Create Examples as Tests
*Make a list of examples of what the function will take and return.*

# Test for empty string as an argument
## task_tracker("") => "Warning! Empty text entered!"

 # Test for a number as an argument
 ## task_tracker(19) => "Warning! No text was entered!"

 # Test a string that includes the string #TODO:
 ## task_tracker("#TODO: Walk the dog!") => True

 # Test a string that includes the string #TODO
 ## task_tracker("This is a #TODO list!") => True

 # Test a string without #TODO
 ## task_tracker("This is a to-do list") => false

 # Test a string with #todo
 # #task_tracker("This is a #todo list!") => False

 # Test a string with #Todo
 ## task_tracker("This is a #Todo list!") => False

 # Test an uppercase text that contains #TODO
 ## task_tracker("THIS IS A #TODO LIST!") => True

 # Test a text that includes TODO
  ## task_tracker("THIS IS A TODO LIST!") => False

 # Test a text that includes :TODO
   ##  task_tracker("This is a :TODO list!") => False

 # Test a text that includes #T0D0
   ## task_tracker("This is a #T0D0 list!") => False


## 4. Implement the Behaviour
*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

***!! Ensure all test function names are unique, otherwise pytest will ignore them !!***