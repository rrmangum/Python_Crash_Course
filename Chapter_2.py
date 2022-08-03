# A Python print statement that reads Hello FinTech!
print("Hello FinTech!")


# Python Crash Course Chapter 2: Variables and Simple Data Types
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

# variables only contain letters, numbers, and underscores. Must start with a 
# letter. Variable names should be short, but descriptive

message = "Hello Python Crash Crouse reader!"
print(message)

# python interepeter attempts to help you discover your errors
# NameError means we either forgot to set a variable's value before using it or 
# we made a spelling mistake when entering the variable's name.

# Exercise 2-1 Simple Message
'''Store a message in a variable, and then print that
message.
'''
simple_message = "I love Hilo the Dalmatian"
print(simple_message)

#Exercise 2-2 Simple Messages
'''Store a message in a variable, and print that message.
Then change the value of your variable to a new message, and print the new
message.
'''
simple_message = "I love Hilo the Dalmatian"
print(simple_message)
simple_message = "I love Nathalie my wife"
print(simple_message)

# strings is a series of characters; anything inside quotations is a string in 
# Python
"This is a string."
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named are Monty Python, not the snake."

# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())

# method title() apepars after teh variable in the print() statement. A method 
# is an action that Python can perform on a piece of data. the (.) after name in
# name.title() tells Python to make the title() method act on the variable name.
# title() displays each word in titlecase, where each word begins with a capital
# letter. You might want your computer to recognize Ada, ADA, and ada as the 
# same name and display all of them as Ada.

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# lower method is useful for storing data. You won't trust capitilization that 
# users provide so you convert strings to lowercase before storing them. When 
# you want to display the information use the case that makes the most sense for
# each string.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# combing strings like the example above is called concatenation. This can be 
# used to compose complete messages using the information you stored as a 
# variable.
print("Hello, " + full_name.title() + "!")

# concatenation
message = "Hello, " + full_name.title() + "!"
print(message)

# adding whitespace to Strings with Tabs or Newlines
# whitespace = spaces, tabs, and end of line symbols; used to organize outputs 
# so it's easier for users to read.
# add a tab = \t
print("python")
print("\tPython")

# add a newline = \n
print("Languages:\nPython\nC\nJavaScript")

# remove whitespace temporarily from right side of string
# variable_name.rstrip()
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)
print(favorite_language.strip())

# remove whitespace permanently by storing the stripped value back into the 
# variable
favorite_language = favorite_language.rstrip()
print(favorite_language)

# remove whitespace temporarily from left side of string
# variable_name.lstrip()
# remove whitespace tempprarily from both sides of string 
# variable_name.strip()

# strip() function is used mainly to clean up user input before it's stored in a
# program

# avoiding syntax error with strings
# syntax errors occur when Python doesn't recognize a section of your program as
# valid Python code

message = "One of Python's strengths is its diverse community."
print(message)

# Exercise 2-3 Personal Message
'''Store a person's name in a variable, and print a message to that person. 
Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?
'''
name = "Nathalie Lozano"
print("Hello, " + name + "!")

#Exercise 2-4 Name Cases
'''Store a person's name in a variable, and then print that person's name in 
lowercase, uppercase, and titlecase.
'''
name = "Nathalie Lozano"
print("Hello, " + name.title() + "!")
print("Hello, " + name.upper() + "!")
print("Hello, " + name.lower() + "!")

# Exercise 2-5 Famous Quote
'''Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
'''
quote = "Through Endurance We Conquer"
print("Sir Ernest Shackleton once said, " + quote)

# Exercise 2-6 Famous Quote 2:
'''Repeat Exercise 2-5, but this time store the famous person's name 
in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.
'''
famous_person = "Sir Ernest Shackleton"
quote = "Through Endurance We Conquer"
message = famous_person + " once said, " + quote
print(message)

# Exercise 2-7 Stripping Names
'''Store a person's name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''
name = "\tRyan"
second_name = "\nNathalie"
print(name)
print(second_name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(second_name.lstrip())
print(second_name.rstrip())
print(second_name.strip())

# a float is any number with decimals
# sometimes python will interepret numbers as numerical values or strings.
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)
# this code returns a TypeError because the computer doesn't know to represent 
# 23 as twenty-three or two then three
# string the values together so python knows what you're trying to tell it
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Exercise 2-8 Number Eight:
'''Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print statements to see the results.Your output should simply be four lines 
with the number 8 appearing once on each line.
'''
addition = 4 + 4
print(addition)
subtraction = 17 - 9
print(subtraction)
multiplication = 2 * 2 * 2
print(multiplication)
division = 16 / 2
print(division)

# Exercise 2-9 Favaorite Number
favorite_number = 69
print("My favorite number is, " + str(favorite_number) + "!")

# The Zen of Python, by Tim Peters
# Beutiful is better than ugly
# simple is better than complex
# complex is better than complicated
# readability counts
# there should be one-- and preferably only one --obvious way to do it
# now is better than never
