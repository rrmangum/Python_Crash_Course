
# A Python print statement that reads Hello FinTech!
print("Hello FinTech!")


# Python Crash Course Chapter 2: Variables and Simple Data Types
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

# variables only contain letters, numbers, and underscores. Must start with a letter.
# variable names should be short, but descriptive

message = "Hello Python Crash Crouse reader!"
print(message)

# python interepeter attempts to help you discover your errors
# NameError means we either forgot to set a variable's value before using it or we made a spelling mistake when entering the variable's name.

simple_message = "I love Hilo the Dalmatian"
print(simple_message)

simple_message = "I love Nathalie my wife"
print(simple_message)

# strings is a series of characters; anything inside quotations is a string in Python
"This is a string."
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named are Monty Python, not the snake."

# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())

# method title() apepars after teh variable in the print() statement. A method is an action that Python can perform on a piece of data.
# the (.) after name in name.title() tells Python to make the title() method act on the variable name.
# title() displays each word in titlecase, where each word begins with a capital letter. 
# you might want your computer to recognize Ada, ADA, and ada as the same name and display all of them as Ada.

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# lower method is useful for storing data. You won't trust capitilization that users provide so you convert strings to lowercase before storing them.
# when you want to display the information use the case that makes the most sense for each string.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# combing strings like the example above is called concatenation. This can be used to compose complete messages using the information you stored as a variable.
print("Hello, " + full_name.title() + "!")

# concatenation
message = "Hello, " + full_name.title() + "!"
print(message)

# adding whitespace to Strings with Tabs or Newlines
# whitespace = spaces, tabs, and end of line symbols; used to organize outputs so it's easier for users to read.
# add a tab = \t
print("python")
print("\tPython")

# add a newline = \n
print("Languages:\nPython\nC\nJavaScript")

# remove whitespace temporarily from right side of string = variable_name.rstrip()
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)
print(favorite_language.strip())

# remove whitespace permanently by storing the stripped value back into the variable
favorite_language = favorite_language.rstrip()
print(favorite_language)

# remove whitespace temporarily from left side of string = variable_name.lstrip()
# remove whitespace tempprarily from both sides of string = variable_name.strip()

# strip() function is used mainly to clean up user input before it's stored in a program

# avoiding syntax error with strings
# syntax errors occur when Python doesn't recognize a section of your program as valid Python code

message = "One of Python's strengths is its diverse community."
print(message)

name = "Nathalie Lozano"
print("Hello, " + name.title() + "!")
print("Hello, " + name.upper() + "!")
print("Hello, " + name.lower() + "!")

quote = "Through Endurance We Conquer"
author = "Sir Ernest Shackleton"
print(author + " once said, " + quote)

message = author + " once said, " + quote
print(message)

name = "\tRyan"
print(name)
print(name.lstrip())

# a float is any number with decimals
# sometimes python will interepret numbers as numerical values or strings.
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)
# this code returns a TypeError because the computer doesn't know to represent 23 as twenty-three or two then three
# string the values together so python knows what you're trying to tell it
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

addition = 4 + 4
print(addition)
subtraction = 17 - 9
print(subtraction)
multiplication = 2 * 2 * 2
print(multiplication)
division = 16 / 2
print(division)

favorite_number = 69
print("My favorite number is, " + str(favorite_number) + "!")

# The Zen of Python, by Tim Peters
# Beutiful is better than ugly
# simple is better than complex
# complex is better than complicated
# readability counts
# there should be one-- and preferably only one --obvious way to do it
# now is better than never
