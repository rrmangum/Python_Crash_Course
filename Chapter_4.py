# Chapter 4 - Working with Lists

# for loops is a useful function for conductin the same action on every item within a list

magicians = ['alice', 'david', 'carolina'] # define the list
for magician in magicians: # define a for loop, telling python to pull a name from the list magicians and store it in the variable magician
    print(magician) # print the name that was just stored in magician

# python will repeat the for line and the print line fo each name in the list.
# read this code as 
    # "FOR EVERY MAGICIAN IN THE LIST OF MAGICIANS, PRINT THE MAGICIAN'S NAME"

# looping is very important because it's one of the most common ways a computer automates repetitive tasks

# for magician in magicians: tells python to retrieve the first value from the list magicians ans store it in the variabale magician. the first value being 'alice'
# print(magician) tells python to print the current value of magician and then python returns to the first line of the loop
# python retrieves the next name on the list 'david' and stores that value in magician. python then executes the print function again

# the set of steps is repeated for each item in the list, no matter how many items are in the list.
# keep in mind when writing your own for loops that you can choose any name you want for the temp variable that holds each value in the list.
# choose something meaningful that represents a single item from the list.
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

magicians = ['alice', 'david', 'carolina'] # define the list
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# every indented line following the line for magician in magicians is considered inside the loop
# each indented line is executed once for each value in the list.

magicians = ['alice', 'david', 'carolina'] # define the list
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# usually after completing necessary work with a list you want to summarize a block of output or move on to other work that your program must accomplish
print("Thank you, everyone. That was a great magic show!")

# In a logical error the syntax is valid Python code, but the code does not produce the desired result because a problem occurs in its logic

favorite_pizza = ["supreme", "pepperoni", "margherita"]
for pizza in favorite_pizza:
    print("I like " + pizza.lower() + " pizza.")
print("Man, I love pizza so much.")

common_animals = ["dog", "cat", "bird"]
for animal in common_animals:
    print("A " + animal.lower() + " would make a great pet.\n")
print("These animals all make great pets!")

# the range function makes it easy to generate a series of numbers
for value in range(1,6):
    print(value)

# you can use the range function to create a list of numbers
numbers = list(range(1,6))
print(numbers)

# can also use python to skip numbers in a given range
even_numbers = list(range(2,11,2))
print(even_numbers)
# the range function starts with the value 2 and then adds 2 to that value until it reaches or passes the end value, 11.

squares = [] # empty list
for value in range(1,11): # loop through each value from 1 to 10
    square = value**2 # current value is raised to the second power and stored in the variable square
    squares.append(square) # new value of square is appended to the list squares
print(squares)

# clean up the code by omitting the temporary variable square and append each new value directly to the list
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# list comprehension allows you to generate a list in one line of code by combining a for loop and the creation of new elements ino one line and automatically appends each new element.
squares = [value**2 for value in range (1,11)]
print(squares)
# define the expression
# write a for loop to generate the numbers you want to feed into the expression
# do not include a colon

# numbers = list(range(1,21))
# print(numbers)
# numbers = list(range(1,1000001))
# print(numbers)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

numbers = list(range(1,21,2))
print(numbers)

threes = list(range(3,31,3))
print(threes)

cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)

# slicing a list by specifying the index of the first and last elements you want to work with

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) # if you omit the first index in a slice, Python automatically starts slice as the beinning of the list
print(players[2:]) # slice to the end of the list
print(players[-3:]) # any point on the list to the end even with changes to the list

# looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My new favorite foods are:")
print(my_foods)

print("\nMy friend's new favorite foods are:")
print(friend_foods)
 
print("The first three items in the list are:")
print(players[0:3])

print("Three items from the middle of the list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[2:5])

favorite_pizza = ["supreme", "pepperoni", "margherita"]
friend_favorite_pizza = favorite_pizza[:]

favorite_pizza.append("El Camino")
friend_favorite_pizza.append("BBQ Chicken")

print("My favorite pizzas are: ")
for pizza in favorite_pizza:
    print(pizza.title())

print("My friend's favorite pizzas are: ")
for pizza in friend_favorite_pizza:
    print(pizza.title())

# a Tuple is an immutable list
# use parentheses instead of brackets

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# you can't change items withing a tuple, but you can assign a new value to a variable that holds a tuple

print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

buffet_foods = (
    "Salad",
    "Ribs",
    "Lasagna",
    "Tacos",
    "Grilled Chicken"
)

for food in buffet_foods:
    print(food)

new_buffet_foods = (
    "Salad",
    "Stir-Fry",
    "Lasagna",
    "Sandwiches",
    "Grilled Chicken"
)
print(buffet_foods)
print(new_buffet_foods)

# 79 characters max length per line of code
# comments limited to 72 characters
