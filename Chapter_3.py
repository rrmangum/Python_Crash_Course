# Chapter 3 - Introducing Lists
# a list is collection of items in a particular order
# [] indicate a list and individual elements in the list are separated by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# you can tell python to access any item in a list through its indexed position
# write the name of the list followed by the index of the item enclosed in 
# square brackets

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())

# access the last element in a list through index -1; second to last item can 
# be accessed by -2 and so on
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Exercise 3-1 Names
'''
Store the names of a few of your friends in a list called names. Print
each person's name by accessing each element in the list, one at a time.
'''
ryan_friend_names = ['Elliott', 'Tommy', 'Allie', 'Zach', 'Ethan', 'Joe']
print(ryan_friend_names[0].title())
print(ryan_friend_names[1].title())
print(ryan_friend_names[2].title())
print(ryan_friend_names[3].title())
print(ryan_friend_names[4].title())
print(ryan_friend_names[5].title())

# Exercise 3-2 Greetings
''' 
Start with the list you used in Exercise 3-1, but instead of just
printing each person's name, print a message to them. The text of each 
message should be the same, but each message should be personalized with the
person's name.
'''
print("Hello " + 
    ryan_friend_names[0].title() + 
    ", it's nice to see you again."
)
print("Hello " + 
    ryan_friend_names[1].title() + 
    ", it's nice to see you again."
)
print("Hello " + 
    ryan_friend_names[2].title() + 
    ", it's nice to see you again."
)
print("Hello " + 
    ryan_friend_names[3].title() + 
        ", it's nice to see you again."
)
print("Hello " + 
    ryan_friend_names[4].title() + 
    ", it's nice to see you again."
)
print("Hello " + 
    ryan_friend_names[5].title() + 
    ", it's nice to see you again."
)

# Exercise 3-3 Your Own List
'''
Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own 
a Honda motorcycle.”
'''
vehicles = ['Sailboat', 'Tesla', 'Pickup Truck', 'Skateboard']

print("I would love to own a " + 
    vehicles[0].lower() + 
    " and sail around the Hawaiian Islands"
)
print("I would like to purchase a " + 
    vehicles[1].lower() + 
    " and save money on gasoline."
)
print("I will eventually buy an old " + 
    vehicles[2].lower() + 
    " and restore it to its former glory."
)
print("I used to " + 
    vehicles[3].lower() + 
    " with my younger brother."
)

# update lists with a replaced value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# add elements to a list - append the item to the list, the new element is 
# added to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# you can create an empty list and then add data as you receive it once the 
# program is running as expected. This puts the users in control
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# add a new element to any position using the insert() method, must specify the 
# index of the new element and the value of the new item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove items from a list 
# if you know the position of the item you want to remove you use the del 
# statement
del motorcycles[0]
print(motorcycles)

# removing an item using the pop() method
# pop() removes the last item in a list, but it lets you work with that 
# item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# can pop() any item in a list at any position by the index
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# if you don't know the position of the value you want to remove you can use 
# the remove() method if you know the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# you can work with a vlue thats being removed from a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# remove only deletes the first occurrence of the value specified. If the value 
# appears more than once in the list you need to use a loop - see chapter 7

# Exercise 3-4 Guest List
'''
If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you'd like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''
dinner_guests = ['Alan Turing', 'Eleanor Roosevelt', 'Barack Obama']

print("I'd like to invie " + dinner_guests[0] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[1] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[2] + " to my dinner party.")

# Exercise 3-5 Changing Guest List
'''You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think 
of someone else to invite.

-> Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can't make it.

-> Modify your list, replacing the name of the guest who can't make it with
the name of the new person you are inviting.

-> Print a second set of invitation messages, one for each person who is still
in your list.
'''
print("I'd like to invie " + dinner_guests[0] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[1] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[2] + " to my dinner party.")

print(dinner_guests[2] + 
    " has informed the host that " + 
    dinner_guests[0] + 
    " can't make it. He sends his apologies."
)

del dinner_guests[0]
dinner_guests.append('Hilo Rose Mangum')

print("I'd like to invie " + dinner_guests[0] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[1] + " to my dinner party.")
print("I'd like to invie " + dinner_guests[2] + " to my dinner party.")

# Exercise 3-6 More Guests
'''
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

-> Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.

->Use insert() to add one new guest to the beginning of your list.

-> Use insert() to add one new guest to the middle of your list.

-> Use append() to add one new guest to the end of your list.

-> Print a new set of invitation messages, one for each person in your list.
'''
print(dinner_guests[0] + 
    ", " + dinner_guests[1] + 
    ", and " + dinner_guests[2] + 
    " I have found a bigger table and more guests will be joining our dinner")

dinner_guests.insert(0, 'Hunter S. Thompson')
dinner_guests.insert(2, 'Joseph Hernandez')
dinner_guests.insert(5, 'Elliott Hamilton')

print("I want to invite you, " + dinner_guests[0] + " to my dinner party.")
print("I want to invite you, " + dinner_guests[1] + " to my dinner party.")
print("I want to invite you, " + dinner_guests[2] + " to my dinner party.")
print("I want to invite you, " + dinner_guests[3] + " to my dinner party.")
print("I want to invite you, " + dinner_guests[4] + " to my dinner party.")
print("I want to invite you, " + dinner_guests[5] + " to my dinner party.")

# Exercise 3-7 Shrinking Guest List
'''
You just found out that your new dinner table won't
arrive in time for the dinner, and you have space for only two guests.

-> Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.

-> Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you're sorry you can't invite
them to dinner.

-> Print a message to each of the two people still on your list, letting them
know they're still invited.
-
> Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''
print("I can only invite two people to dinner now," 
    "as my new table will not arrive in time")

first_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + first_removed + ".")

second_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + second_removed + ".")

third_removed = dinner_guests.pop(0)
print("I am sorry to have un-invited you, " + third_removed + ".")

fourth_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + fourth_removed + ".")

print(dinner_guests[0] + 
    " and " + 
    dinner_guests[1] + 
    " you both are still invited to dinner.")

del dinner_guests[:]
print(dinner_guests)

# python can sort lists using the sort() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # cannot be reserved to the original order
print(cars)

# reverse alphabetical order through reverse=True
cars.sort(reverse=True) # permanent order change
print(cars)

# to maintain original order, but present in a sorted order use sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# sorting a list alphabetically is more complicated when all the values 
# are not lowercase.

# print the list in reverse order
cars.reverse()
print(cars)

# Exercise 3-8 Seeing the World
'''
Think of at least five places in the world you'd like to visit.

-> Store the locations in a list. Make sure the list is not in 
alphabetical order.

-> Print your list in its original order. Don't worry about printing the 
list neatly, just print it as a raw Python list.

-> Use sorted() to print your list in alphabetical order without modifying the
actual list.

-> Show that your list is still in its original order by printing it.

-> Use sorted() to print your list in reverse alphabetical order without 
changing the order of the original list.

-> Show that your list is still in its original order by printing it again.

-> Use reverse() to change the order of your list. Print the list to show 
that its order has changed.

-> Use reverse() to change the order of your list again. Print the list to show
it's back to its original order.

-> Use sort() to change your list so it's stored in alphabetical order. Print 
the list to show that its order has been changed.

-> Use sort() to change your list so it's stored in reverse alphabetical order.
Print the list to show that its order has changed.
'''
world_vacations = [
    "Egypt", 
    "Spain", 
    "Colombia", 
    "Greece", 
    "Indonesia", 
    "Vietnam"
]
print(world_vacations)

print(sorted(world_vacations))

print(world_vacations)

print(sorted(world_vacations, reverse=True))

print(world_vacations)

world_vacations.reverse()

print(world_vacations)

world_vacations.reverse()

print(world_vacations)

world_vacations.sort()

print(world_vacations)

world_vacations.sort(reverse=True)

print(world_vacations)

# Exercise 3-9 Dinner Guests
'''
Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
'''
print(f"I am inviting {len(dinner_guests)} guests to dinner.")

# Exercise 3-10 Every Function
'''
Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or 
anything else you'd like. Write a program that creates a list containing these 
items and then uses each function introduced in this chapter at least once.
'''
favorite_cuisines = [
    "Mexican", 
    "Korean", 
    "Italian", 
    "Japanese", 
    "Spanish", 
    "French", 
    "Greek"
]

print(favorite_cuisines[1])

message = "My favorite food is " + favorite_cuisines[0] + "!"
print(message)

favorite_cuisines[5] = "American"
print(favorite_cuisines)

favorite_cuisines.append("French")
print(favorite_cuisines)

favorite_cuisines.insert(1, "German")
print(favorite_cuisines)

del favorite_cuisines[1]
print(favorite_cuisines)

popped_cuisine = favorite_cuisines.pop(2)
print(popped_cuisine)

favorite_cuisines.remove("American")
print(favorite_cuisines)

favorite_cuisines.sort()
print(favorite_cuisines)

# if you're getting errors when working with lists, print the list or ask 
# for the len of the list. The list you're working with may be different 
# than you thought.

