# The input function pauses the program and waits for the user to 
# enter some text

message = input("Tell me something, and I will reapeat it back to you: ")
print(message)

# It takes one arguement: the prompt or instructions that we want to 
# display to the user
# Can also pass variables as the arguement

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Python intereprets everything entered by the user as a string

age = input("How old are you? ")
print(type(age)) # ---> This returns a str
# age>=18 #---> produces a TypeError

# Can't use numbers that are formatted as strings in mathematical calculations
# Must use int() function to treat the input as a numerical value and not a 
# string

age = input("How old are you? ")
age = (int(age))
age >= 18 # ---> returns True

# Example in an actual program

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")

# The modulo operator only returns the remainder

# 4 % 3 #---> 1
# 5 % 3 #---> 2
# 6 % 3 #---> 0

# Determine if numbers are even or odd:
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")

# Exercise 7-1 Rental Car
'''
Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can 
find you a Subaru.
'''

rental_car = input("What type of rental car would you like? ")
rental_car = rental_car.lower()

if rental_car == "subaru":
    print("You're in luck, we have a Subaru available!")
elif rental_car == "jeep":
    print("I'm sorry, we don't have any Jeeps available. They rent out fast.")
elif rental_car == "tesla":
    print("What do you think this is? Some high class car rental company?")

# Exercise 7-2 Restaurant Seating
'''
Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message 
saying they'll have to wait for a table. Otherwise, report that their 
table is ready
'''

dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group >= 8:
    print("I'm sorry, but you'll have to wait 25 minutes for a table.")
else:
    print("We have a table ready for you now, right this way.")

# Exercise 7-3 Multiples of Ten
''' Ask the user for a number, and then report whether the
number is a multiple of 10 or not
'''
user_number = input("Enter a number and I'll tell you if its a multiple" 
    " of 10 or not: ")
user_number = int(user_number)

if user_number % 10 == 0:
    print(f"\nThe number {user_number} is a multiple of 10.")
else:
    print(f"\nThe number {user_number} is not a multiple of 10.")

# The for loop takes a collection of items and executes a block of code once 
# for each item in the collection. 
# In contrast, the while loop runs as long as, or while, a certain 
# condition is true.

# Use a while loop to count up through a series of numbers
current_number = 1

while current_number <= 5:
 print(current_number)
 current_number += 1

# Let the user decide when to quit the program

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# += is telling Python prompt = prompt + "\nEnter 'quit' to end the program." 
# its just a shorthand version

message = ""

while message != 'quit':
    message = input(prompt)
    
    if message !='quit':
        print(message)

# a flag acts as signal to the program. Used in a program that should run 
# only as long as many conditions are true, you can define one variable that 
# determines whether or not the entire program is active write programs so they 
# run while the flag is set to True and stop running when any of the several 
# events sets the value of the flag to False this while statement only needs to 
# check one condition: whether or not the flag is currently True
# all other tests can be organized in the rest of the program

active = True # this is the flag, and can be named anything just like a variable
while active: # loop continues running as long as the flag remains True
    message = input(prompt)

#  if user enters 'quit' change the flag to False and the loop stops
    if message == 'quit': #
        active = False
    else: 
        print(message)
# if user enters anything other than 'quit' print their input as a message

# this program is the same output as the previous exercise, but the program is 
# more organized and will be much easier to add future conditions in which the 
# program should end

# the break statement will exit a while loop immediately without running any 
# remaining code regardless of the results of any conditional test
# it can be used to control which lines of code are executed and which aren't.
prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)"

# a loop that starts with while True will run forever 
#unless it reaches a break statement
while True: 
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# you can use the break statement in any Python loop, even in an for loop 
# working through a list or dicitionary

# use the continue statement to return to the beginning of the loop based on 
# the result of a conditional test
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: 
        continue
    print(current_number)
# if statement checks the modulo of current_number and 2, if the modulo is 0, 
# the continue statement tells Python to ignore the rest of the loop and return 
# to the beginning

# every while loop needs a way to stop so it doesn't continue to run forever
# a counting loop that counts from 1 to 5 and ends
x = 1
while x <= 5:
    print(x)
    x += 1

# no end
x = 1
while x <= 5:
    print(x)

# if you accidentally write an inifinte while loop, just hit ctrl-c or close your terminal

# Exercise 7-4 Pizza Toppings
'''Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you'll add that topping to their pizza.
'''

prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' to end the program"
prompt += "\n"

flag = True
while flag:
    message = input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(f"I'm adding {message} to your pizza!")

# Exercise 7-5 Movie Tickets
'''
A movie theater charges different ticket prices depending on
a person's age. If a person is under the age of 3, the ticket is free; if they 
are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket
is $15. Write a loop in which you ask users their age, and then tell them the 
cost of their movie ticket.
'''
prompt = "\nWhat is your age?"
prompt += "\n"

age = int(input(prompt))

if age < 3:
    ticket_price_free = '$0'
    print(f"Your ticket costs {ticket_price_free}.")
elif (age >= 3) and (age <= 12):
    ticket_pice_middle = '$10'
    print(f"Your ticket costs {ticket_pice_middle}.")
elif age > 12:
    ticket_price_expensive = '$15'
    print(f"Your ticket costs {ticket_price_expensive}.")

# Exercise 7-6 Three Exits
'''
Write different versions of either Exercise 7-4 or Exercise 7-5 that do each 
of the following at least once:

-> Use a conditional test in the while statement to stop the loop.

-> Use an active variable to control how long the loop runs.

-> Use a break statement to exit the loop when the user enters a 'quit' value.
'''
prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' to end the program"
prompt += "\n"

# active variable
flag = True
while flag:
    message = input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(f"I'm adding {message} to your pizza!")

# break statement
while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"I'm adding {message} to your pizza!")

# conditional test
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(f"I'm adding {message} to your pizza!")

# Exercise 7-7 Infinity
'''
Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.
'''

x = 1
while x <= 5:
    print(x)

# instead of for loops to modify a list, use a while loop. This allows you to 
# collect, store, and organize lots of input to examine and report on later

# move items from one list to another

# start with users that need to be verified, and an empty list to hold 
# confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users. Move each 
# verified user into the list of confirmed users

# loop runs as long as the list of unconfirmed_users is not empty
# removes unverified users one at a time from the end of unconfirmed_users
# add users to the confirmed_users list
while unconfirmed_users: 
    current_user = unconfirmed_users.pop() 

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) 

# display all confirmed users
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# remove all instances of a value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# filling a dictionary with user input
responses = {}

# set a flag to indicate polling is active
polling_active = True

while polling_active:
    # prompt for the user's name and response
    name = input(f"\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete show the results
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Exercise 7-8 Deli
'''
Make a list called sandwich_orders and fill it with the names of various 
sandwiches. Then make an empty list called finished_sandwiches. Loop through the
list of sandwich orders and print a message for each order, such as I made your 
tuna sandwich. As each sandwich is made, move it to the list of finished 
sandwiches. After all the sandwiches have been made, print a message listing 
each sandwich that was made
'''
sandwich_orders = ['BLT', 'Tuna Melt', 'Grilled Cheese', 'Club', 'Italian']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")

    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")

# Exercise 7-9 No Pastrami
'''
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
'''
sandwich_orders = [
    'BLT', 
    'Pastrami', 
    'Tuna Melt', 
    'Grilled Cheese', 
    'Pastrami', 
    'Club', 
    'Italian', 
    'Pastrami'
]

print(f"The deli has run out of Pastrami")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(f"\nThe available sandwiches from the deli are:")
print(f"{sandwich_orders}")

# Exercise 7-10 Dream Vacation
'''
Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''
responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit on place in the world, " 
    "where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let others respond to the poll? (yes/no)")
    if repeat == 'no':
        poll_active = False

print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")

    