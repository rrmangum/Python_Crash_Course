# if statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': # checks to see if current value is bmw
        print(car.upper()) # prints in all caps
    else: # everything else that is not bmw
        print(car.title()) # prints in title case

# conditional tests are a check for true or false
# if a conditional evaluates to True, Python executes the code following 
# the if statement
# if a conditional evaluates to False, Python ignores the code following the 
# if statement

car = 'bmw' 
car == 'bmw' 
# will evaluate to True

car = 'audi' # "Set the value of far equal to 'audi'" - A STATMENT
car == 'bmw' # "Is the value of car equal to 'bmw'?" - A QUESTION
# will evaluate to False

# two values with different capitalization are not considered equal:
car = 'Audi'
car == 'audi'
# will evaluate to False

car = 'Audi'
car.lower() == 'audi'
# will evaluate to false because you're forcing the variable to assume all 
# lowercase characters is used to compare usernames and ensure unique-ness 
# instead of case sensitive versions

# can check for inequality with !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# numerical comparisons
age = 18
age == 18
# true

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21 # true
age <= 21 # true
age > 21 # false
age >= 21 # false

# to check if two conditions are both true simultaneously use keyword 'and'. 
# if either test fails or they both fail, the overall expression evaluates to 
# False
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # false

age_1 = 22
age_0 >= 21 and age_1 >= 21 # true

# should use parenthese to increase readability
(age_0 >= 21) and (age_1 >= 21)

# use keyword 'or' to check multiple conditions, this passes as true when 
# either or both of the individual tests pass.
age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21) # true

age_0 = 18
(age_0 >= 21) or (age_1 >= 21) # false

# check wheter a value is in a list with the keyword 'in'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings # true
'pepperoni' in requested_toppings # false

# check whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: # true
    print(user.title() + ", you can post the response if you wish.")

# boolean = conditional test
game_active = True
can_edit = False

# Exercise 5-1 Conditional Tests
'''
Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test.

-> Look closely at your results, and make sure you understand why each line
evaluates to True or False.

-> Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
'''
dog = 'Dalmatian'
print("Is dog == 'Dalmatian'? I predict True.")
print(dog == 'Dalmatian')
print(dog == "Great Dane")

cat = 'Leopard'
print("Is cat == 'Leopard'? I predict True.")
print(cat == 'Leopard')
print(cat == 'Jaguar')

girl = 'Vanessa'
print("Is girl == 'Vanessa'? I predict True.")
print(girl == 'Vanessa')
print(girl == 'LaFawnduh')

guy = 'Thomas'
print("Is guy == 'Thomas'? I predict True.")
print(guy == 'Thomas')
print(guy == 'Bob')

computer = 'Desktop'
print("Is computer == 'Desktop'? I predict True.")
print(computer == 'Desktop')
print(computer == 'Laptop')

string = "Hello, my name is Ryan."
print(string == "Goodbye.")

# the simplest kind of if statement has one test and one action
# if conditional_test:
#     do something

age = 18
if age >= 19:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else statements, one action for a pass and one action for a fail
if age >= 19:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# to test more than two possible situations use if-elif-else chain
# Python will execute only one block in an if-elif-els chain. It runs each 
# conditional test in order until one passes, and then skips the others.

# An amusement park that charges different rates for different age groups
    # Admission for anyone under age 4 is free.
    # Admission for anyone between the ages of 4 and 18 is $5.
    # Admission for anyone age 18 or older is $10.
age =12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# DRY version
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print(f"Your admission cost is ${str(price)}.")

# if-elif-else chain is only appropiate to use when you just need one test to 
# pass. As soon as Python finds one test that passes, it skips the rest of 
# the tests.
# if you need to check all of the conditions of interest, use a series of simple
# if statements with no elif or else blacks.
# This technique is used when more than one condition could be True, 
# and you want to act on every condition that is True.

# if you want only one block of code to run, use an if-elif-else chain. 
# If more than one block of code needs to run, use a series of 
# independent if statements.

# Exercise 5-3 Alien Colors #1
'''
Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 
'green', 'yellow', or 'red'.

-> Write an if statement to test whether the alien's color is green. If it 
is, print a message that the player just earned 5 points.

-> Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
'''
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points!")

# Exercise 5-4 Alien Colors #2
'''
Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.

-> If the alien's color is green, print a statement that the player just earned
5 points for shooting the alien.

-> If the alien's color isn't green, print a statement that the player 
just earned 10 points.

-> Write one version of this program that runs the if block and another that
runs the else block.
'''
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = "red"

if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

# Exercise 5-5 Alien Colors #3
'''
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

-> If the alien is green, print a message that the player earned 5 points.

-> If the alien is yellow, print a message that the player earned 10 points.

-> If the alien is red, print a message that the player earned 15 points.

-> Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

# Exercise 5-6 Stages of Life
'''
Write an if-elif-else chain that determines a person's
stage of life. Set a value for the variable age, and then:

-> If the person is less than 2 years old, print a message that the person is
a baby.

-> If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.

-> If the person is at least 4 years old but less than 13, print a message that
the person is a kid.

-> If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.

-> If the person is at least 20 years old but less than 65, print a message that
the person is an adult.

-> If the person is age 65 or older, print a message that the person is an
elder.
'''
person_age = 12

if person_age < 2:
    print("You are a baby!")
elif person_age >= 2 and person_age < 4:
    print("You are a toddler!")
elif person_age >= 4 and person_age < 13:
    print("You are a kid!")
elif person_age >= 13 and person_age < 20:
    print("You are a teenager")
elif person_age >= 20 and person_age < 65:
    print("You are an adult")
elif person_age >= 65:
    print("You are an elder")

# Exercise 5-7 Favorite Fruit
'''
Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.

-> Make a list of your three favorite fruits and call it favorite_fruits.

-> Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a 
statement, such as You really like bananas!
'''
favorite_fruits = ["pinneapple", "watermelon", "apple"]

if "pinneapple" in favorite_fruits:
    print("You really like pinnapple!")

if "banana" in favorite_fruits:
    print("You really like banana!")

if "watermelon" in favorite_fruits:
    print("You really like watermelon!")

if "blackberry" in favorite_fruits:
    print("You really like blackberry!")

if "apple" in favorite_fruits:
    print("You really like apple!")

# Exercise 5-8 Hello Admin
'''
Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:

-> If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?

-> Otherwise, print a generic greeting, such as Hello Eric, thank you for 
logging in again.
'''
usernames = [
    "brokiddude", 
    "losebag", 
    "iamthechampion", 
    "suxcoxndix", 
    "iluv69", 
    "admin"
]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, how are you today?")

# Exercise 5-9 No Users
'''
Add an if test to hello_admin.py to make sure the list of users is
not empty.

-> If the list is empty, print the message We need to find some users!

-> Remove all of the usernames from your list, and make sure the correct
message is printed.
'''
usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, how are you today?")
else:
     print("We need to find some users")

# Exercise 5-10 Checking Usernames
'''
Do the following to create a program that simulates
how websites ensure that everyone has a unique username.

-> Make a list of five or more usernames called current_users.

-> Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.

-> Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.

-> Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
'''
current_users = [
    "brokiddude", 
    "losebag", 
    "iamthechampion", 
    "suxcoxndix", 
    "iluv69", 
    "admin"
]

new_users = ["elopoid", 
    "brokiddude", 
    "augustus", 
    "ina", 
    "losebag"
]

for user in new_users:
    if user.lower() in current_users:
        print(f"This username: {user}, is taken, please enter a" 
        "different username.")
    else:
        print(f"This username: {user} is available.")

# Exercise 5-11 Ordinal Numbers
'''
Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

-> Store the numbers 1 through 9 in a list.

-> Loop through the list.

-> Use an if-elif-else chain inside the loop to print the proper ordinal 
nding for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
'''
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for number in numbers:
    if number == "1":
        print(f"{number}st")
    elif number == "2":
        print(f"{number}nd")
    elif number == "3":
        print(f"{number}rd")
    else:
        print(f"{number}th")