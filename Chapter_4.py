# Chapter 4 - Working with Lists

# for loops is a useful function for conductin the same action on 
# every item within a list

# define a for loop, telling python to pull a name from the list 
# magicians and store it in the variable magician
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician)

# python will repeat the for line and the print line fo each name in the list.
# read this code as 
    # "FOR EVERY MAGICIAN IN THE LIST OF MAGICIANS, PRINT THE MAGICIAN'S NAME"

# looping is very important because it's one of the most common 
# ways a computer automates repetitive tasks

# for magician in magicians: tells python to retrieve the first value from the 
# list magicians and store it in the variabale magician. the first value being 
# 'alice'
# print(magician) tells python to print the current value of magician and then 
# python returns to the first line of the loop
# python retrieves the next name on the list 'david' and stores that 
# value in magician. python then executes the print function again

# the set of steps is repeated for each item in the list, no matter 
# how many items are in the list.
# keep in mind when writing your own for loops that you can choose any name you 
# want for the temp variable that holds each value in the list.
# choose something meaningful that represents a single item from the list.
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

magicians = ['alice', 'david', 'carolina'] # define the list
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# every indented line following the line for magician in magicians is 
# considered inside the loop
# each indented line is executed once for each value in the list.

magicians = ['alice', 'david', 'carolina'] # define the list
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# usually after completing necessary work with a list you want to summarize a 
# block of output or move on to other work that your program must accomplish
print("Thank you, everyone. That was a great magic show!")

# In a logical error the syntax is valid Python code, but the code does not 
# produce the desired result because a problem occurs in its logic

# Exercise 4-1 Pizzas
'''
Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.

-> Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.

-> Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
'''
favorite_pizza = ["supreme", "pepperoni", "margherita"]

for pizza in favorite_pizza:
    print("I like " + pizza.lower() + " pizza.")
print("Man, I love pizza so much.")

# Exercise 4-2 Animals
'''
Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.

-> Modify your program to print a statement about each animal, such as
A dog would make a great pet.

-> Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
'''
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
# the range function starts with the value 2 and then adds 2 to that value 
# until it reaches or passes the end value, 11.

squares = [] # empty list
for value in range(1,11): # loop through each value from 1 to 10
    square = value**2 # current value is raised to the second power 
    squares.append(square) # new value of square is appended to the list squares
print(squares)

# clean up the code by omitting the temporary variable square and append 
# each new value directly to the list
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# list comprehension allows you to generate a list in one line of code by 
# combining a for loop and the creation of new elements ino one line and 
# automatically appends each new element.
squares = [value**2 for value in range (1,11)]
print(squares)
# define the expression
# write a for loop to generate the numbers you want to feed into the expression
# do not include a colon

# Exercise 4-3 Counting to Twenty
'''
Use a for loop to print the numbers from 1 to 20,
inclusive.
'''
numbers = list(range(1,21))
print(numbers)

# Exercise 4-4 One Million
'''
Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing ctrl-C or by closing the output window.)
'''
numbers = list(range(1,1000001))
print(numbers)

# Exercise 4-5 Summing a Million
'''
Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
'''
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Exercise 4-6 Odd Numbers
'''
Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number
'''
numbers = list(range(1,21,2))
for number in numbers:
    print(number)

# Exercise 4-7 Threes
'''
Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list
'''
threes = list(range(3,31,3))
for three in threes:
    print(three)

# Exercise 4-8 Cubes
'''
A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
(that is, the cube of each integer from 1 through 10), and use a for loop to 
print out the value of each cube.
'''
cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
    print(cubes)

# Exercise 4-9 Cube Comprehension
'''
Use a list comprehension to generate a list of the first 10 cubes.
'''
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# slicing a list by specifying the index of the first and 
# last elements you want to work with

# if you omit the first index in a slice, Python automatically 
# starts slice at the beinning of the list
# slice to the end of the list
# any point on the list to the end even with changes to the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) 
print(players[2:]) 
print(players[-3:]) 

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
 
# Exercise 4-10 Slices
'''
Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

-> Print the message, The first three items in the list are:. Then use a 
slice to print the first three items from that program's list.

-> Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.

-> Print the message, The last three items in the list are:. Use a slice to 
print the last three items in the list
'''
print("The first three items in the list are:")
print(players[0:3])

print("Three items from the middle of the list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[-3:])

# Exercise 4-11 My Pizzas, Your Pizzas
'''
Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:

-> Add a new pizza to the original list.

-> Add a different pizza to the list friend_pizzas.

-> Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. 
Print the message, My friend's favorite pizzas are:, and then use a 
for loop to print the second list. Make sure each new pizza is 
stored in the appropriate list.
'''
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

# you can't change items withing a tuple, but you can assign a new value 
# to a variable that holds a tuple

print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

# Exercise 4-13 Buffet
'''
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

-> Use a for loop to print each food the restaurant offers.

-> Try to modify one of the items, and make sure that Python rejects the
change.

-> The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''
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
