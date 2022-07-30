# if statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': # checks to see if current value is bmw
        print(car.upper()) # prints in all caps
    else: # everything else that is not bmw
        print(car.title()) # prints in title case

# conditional tests are a check for true or false
# if a conditional evaluates to True, Python executes the code following the if statement
# if a conditional evaluates to False, Python ignores the code following the if statement

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
# will evaluate to false because you're forcing the variable to assume all lowercase characters
# is used to compare usernames and ensure unique-ness instead of case sensitive versions

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

# to check if two conditions are both true simultaneously use keyword 'and'. if either test fails or they both fail, the overall expression evaluates to False
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # false

age_1 = 22
age_0 >= 21 and age_1 >= 21 # true

# should use parenthese to increase readability
(age_0 >= 21) and (age_1 >= 21)

# use keyword 'or' to check multiple conditions, this passes as true when either or both of the individual tests pass.
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

dog = 'Dalmatian'
print("Is dog == 'Dalmatian'? I predict True.")
print(dog == 'Dalmatian')
print(dog == "Great Dane")

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
# Python will execute only one block in an if-elif-els chain. It runs each conditional test in order until one passes, and then skips the others.

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

if-elif-else chain is only appropiate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests.
if you need to check all of the conditions of interest, use a series of simpel if statements with no elif or else blacks.
This technique is used when more than one condition could be True, and you want to act on every condition that is True.

if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

person_age = 42

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

favorite_fruits = ["pinneapple", "watermelon", "apples"]

if "pinneapple" in favorite_fruits:
    print("You really like pinnapple!")
if "banana" in favorite_fruits:

usernames = ["brokiddude", "losebag", "iamthechampion", "suxcoxndix", "iluv69", "admin"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, how are you today?")
else:
     print("We need to find some users")

current_users = ["brokiddude", "losebag", "iamthechampion", "suxcoxndix", "iluv69", "admin"]

new_users = ["elopoid", "brokiddude", "augustus", "ina", "losebag"]

for user in new_users:
    if user.lower() in current_users:
        print("This username is taken, please enter a different username.")
    else:
        print("This username is available.")

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

