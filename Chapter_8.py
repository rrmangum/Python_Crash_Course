# Defining a Function
# def is the keyword, followed by the name of the function, and then what 
# information the function needs to do its job

def greet_user(): # this function needs no information to do its job
    '''Display a simple greeting.''' 
    print("Hello!") # function body

# function call that tells Python to execute the code in the function
greet_user() 

# passing information to a function
# enter a username in the parentheses of the function's definition
# adding username allows the function to accept any value of username
# the function expects you to proivde a value for username each time you call it

def greet_user(username): # username is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('Nathalie') # nathalie is an arguement

# arguements are information passed from a function call to a function

# Exercise 8-1 Message
"""Write a function called display_message() that prints one sentence 
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
"""

def display_message():
    """Display a simple message"""
    print("I am learning about Python functions!")
display_message()

# Exercise 8-2 Favorite Book
"""Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

def favorite_book(title):
    '''
    A function that accepts the user's favorite book and displays it back to them
    '''
    print(f"One of my favorite books is {title}")

favorite_book("Ready Player One")

# positional arguments
# when you call a function that requires more than one input, you must supply 
# the inputs in the order provided by the parameters

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') 
# describe_pet('harry', 'hamster') would not return the intended result when 
# executing the code
describe_pet('dog', 'Hilo')

# key word arguments
# a name value pair directly associated. they free you from having to worry 
# about correctly ordering your arguments in the function call and clarify the 
# role of each value in the function call

describe_pet(animal_type='hamster', pet_name='harry')

# default values allow you to exclude the corresponding arguement 
# suppose the describe_pet function is mostly used to refer to dogs
# whenever a default value is used it must be listed after all the parameters 
# that don't have default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')

# type errors will occur if you do not supply the function with the correct 
# arguments.

# Exercise 8-3 T-Shirt
'''Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should 
print a sentence summarizing the size of the shirt and the message printed on 
it. Call the function once using positional arguments to make a shirt. Call 
the function a second time using keyword arguments
'''

def make_shirt(size, message):
    print(f"The size of the shirt is {size}, and the message is {message}.")

make_shirt('large', 'shit happens')
make_shirt(size='large', message='shit happens')

# Exercise 8-4 Large Shirts
'''Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a 
different message.
'''
def make_shirt(size='large', message='I love Python'):
    print(f"The size of the shirt is {size}, and the message is {message}.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Dalmatians Rule!')

# Exercise 8-5 Citites
'''Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in
the default country.
'''

def describe_city(city_name, country='USA'):
    print(f"{city_name} is in {country}.")

describe_city('Los Angeles')
describe_city('Honolulu')
describe_city('London', country='UK')

# return statement takes a value from inside a function and sends it back to 
# the line that called the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# optional arguments
# not everyone has a middle name

def get_formatted_name(first_name, last_name, middle_name='' ):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dicitionary
# functions can return any kind of value

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# this function can easily accept otional values
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# use while loops with functions. this is an infinite loop because the program
# is never told to exit
# def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted"""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

# while True:
#    print("\nPlease tell me your name. ")
#    f_name = input("First name: ")
#    l_name = input("Last name: ")

#    formatted_name = get_formatted_name(f_name, l_name)
#    print(f"\nHello, {formatted_name}!")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name. ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Exercise 8-6 City Names
'''
Write a function called city_country() that takes in the name of a city and 
its country. The function should return a string formatted like this:
"Santiago, Chile". Call your function with at least three city-country pairs, 
and print the value that's returned.
'''

def city_country(city, country, state=''):
    "Display a city and its country"
    
    if state:
        formatted = f"{city}, {state}, {country}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()

first_city = city_country('Los Angeles', 'USA', state='California')
second_city = city_country('San Diego', 'USA', state='California')
third_city = city_country('Austin', 'USA', state='Texas')

print(first_city)
print(second_city)
print(third_city)

# Exercise 8-7 Album
"""Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing 
different albums. Print each return value to show that the dictionaries are 
storing the album information correctly.

Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the 
number of tracks, add that value to the album's dictionary. Make at least one 
new function call that includes the number of tracks on an album.
"""

def make_album(artist_name, album_title):
    """"Create a dictionary of album information"""
    album = {"Artist Name": artist_name, "Album Title": album_title}
    return album

print(make_album('Linkin Park', 'Minutes to Midnight'))
print(make_album('Bring Me The Horizon', "That's The Spirit"))
print(make_album('Tash Sultana', 'Flow State'))

def make_album(artist_name, album_title, number_tracks=''):
    """"Create a dictionary of album information"""
    if number_tracks:
        album = {
            "Artist Name": artist_name, 
            "Album Title": album_title, 
            "Number of Tracks": number_tracks
        }
    else:
        album = {"Artist Name": artist_name, "Album Title": album_title}
    return album

print(make_album('Juanes', 'Mas Futuro Que Pasado', '13'))

# Exercise 8-8 User Albums
"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have 
that information, call make_album() with the user's input and print the 
dictionary that's created. Be sure to include a quit value in the while loop.
"""

def make_album(artist_name, album_title, number_tracks=0):
    """Allow users to enter album information from the CLI"""
    album = {
        "Artist Name": artist_name.title(), 
        "Album Title": album_title.title()
        }
    if number_tracks:
        album['Number of Tracks'] = number_tracks
    return album
    
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    
    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

# passing a list to a function gives the function direct access to the 
# contents of the list
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# functions can modify lists. changes made in the function body are permenant
# compare the code below:

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

# Simulate creating a 3D print from the design.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# make the code more efficient by writing two functions, each of which does one 
# specific job. First function handles printing the designs second function 
# summarized the prints that have been made

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # simulate creating a 3D print from the design
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# every function should have one specific job. if a function is doing too many 
# different tasks, split the code into multiple functions
# prevent a function from modifying a list

# function_name(list_name[:])
# slice notation makes a copy of the list to send to the function
# should still send the existing list unless you have a specific use for the 
# copy. it's more effecient when it comes to time and memory needed to make the 
# copy

print_models(unprinted_designs[:], completed_models)

# Exercise 8-9 Magicians
"""Make a list of magician's names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list
"""

magician_names = ['Harry Houdini', 'David Blane', 'Chris Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

show_magicians(magician_names)

# Exercise 8-10 Great Magicians
"""Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by 
adding the phrase the Great to each magician's name. Call show_magicians() to
see that the list has actually been modified.
"""

def make_great(magician_names):
    """
    Add 'The Great' to each magician's name from a provided list. 
    Modifies the list permanently.
    """
    great_magicians = []

    while magician_names:
        magician = magician_names.pop()
        great_magician = magician + " The Great"
        great_magicians.append(great_magician)
        
    for great_magician in great_magicians:
        magician_names.append(great_magician)
    
show_magicians(magician_names)        
make_great(magician_names)
show_magicians(magician_names)
        
# Exercise 8-11 Unchanged Magicians
"""Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians' names. Because 
the original list will be unchanged, return the new list and store it in a 
separate list. Call show_magicians() with each list to show that you have one 
list of the original names and one list with the Great added to each 
magician's name.
"""
magician_names = ['Harry Houdini', 'David Blane', 'Chris Angel']
great_magicians = []

def make_great(magician_names):
    for magician in magician_names:
        magician = f"The Great {magician}"
        great_magicians.append(magician)
        print(magician)

make_great(magician_names.copy())

show_magicians(magician_names)
show_magicians(great_magicians)

# Passing an Arbitrary Number of Arguements - * allows Python to accept any 
# given amount of arguements, because the function design won't know how many 
# arguements are required until the user enters their arguements. The asterisk
# tells Python to make an empty Tuple called toppings and pack whatever values
# it receives into the tuple.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguements
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition. Python matches positional and keyword
# arguments first and then collects any remaining arguments in the final
# parameter.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguements
# Sometimes you'll want to accept an arbitrary number of arguments, but you
# won't know ahead of time what kind of information will be passed to the
# function. In this case, you can write functions that accept as many 
# key-value pairs as the calling statement provides. Double asterisk allows 
# multiple key-value pairs passed to the function. Python creates an empty 
# dictionary called user_info and adds the key-value pairs to this dictionary

def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    'albert', 
    'einstein',
    location='princeton',
    field='physics'
)

print(user_profile)

# Exercise 8-12 Sandwiches
"""
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the 
sandwich that is being ordered. Call the function three times, using a 
different number of arguments each time.
"""
def sandwich_toppings(*toppings):
    """
    Prints the lst of requested toppings
    """
    print("\nYour order consists of the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")

sandwich_toppings("salami", "turkey", "lettuce", "tomato")
sandwich_toppings("bacon", "lettuce", "tomato")
sandwich_toppings("turkey", "cheese", "mayo")

# Exercise 8-13 User Profile
"""
Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last 
names and three other key-value pairs that describe you.
"""
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

ryan_profile = build_profile(
    'Ryan', 
    'Mangum',
    location='Los Angeles',
    field='Software Development',
    spouse='Nathalie'
)

print(ryan_profile)

# Exercise 8-14 Cars
"""
Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this 
one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all the information was
stored correctly.
"""
def car_info(manufacturer, model_name, **options):
    info = {}
    info['manufacturer'] = manufacturer
    info['model_name'] = model_name
    for key, value in options.items():
        info[key] = value
    return info

honda_info = car_info(
    'honda', 
    'accord',
    color = 'black',
    upholstery = 'leather'
)

print(honda_info)

# Storing Your Functions in Modules

# Importing an Entire Module
# import <module_name>

# Importing Specific Functions
# from <module_name> import <function_name>

# Importing More Then One Specific Function
# from <module_name> import <function_name>, <function_name>, <function_name>

# You don't have to use the dot syntax (module_name.function_name()) and instead
#  can just call the function. 
# Because the function has been explicitly imported.

# Using Aliases
# from <module_name> import <function_name> as <fn>
# import <module_name> as <nm>

# Best not to use from module_name import * as this could overwrite functions. 
# use the dot notation.

# Exercise 8-15 Printing Models
"""
Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.
"""
# See Module_Practice

# Exercise 8-16 Imports
"""
Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
"""
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *




