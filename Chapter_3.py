# Chapter 3 - Introducing Lists
# a list is collection of items in a particular order
# [] indicate a list and individual elements in the list are separated by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# you can tell python to access any item in a list through its indexed position
# write the name of the list followed by the index of the item enclosed in square brackets

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())

# access the last element in a list through index -1; second to last item can be accessed by -2 and so on
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

ryan_friend_names = ['Elliott', 'Tommy', 'Allie', 'Zach', 'Ethan', 'Joe']
print(ryan_friend_names[0].title())
print(ryan_friend_names[1].title())
print(ryan_friend_names[2].title())
print(ryan_friend_names[3].title())
print(ryan_friend_names[4].title())
print(ryan_friend_names[5].title())

print("Hello " + ryan_friend_names[0].title() + ", it's nice to see you again.")
print("Hello " + ryan_friend_names[1].title() + ", it's nice to see you again.")
print("Hello " + ryan_friend_names[2].title() + ", it's nice to see you again.")
print("Hello " + ryan_friend_names[3].title() + ", it's nice to see you again.")
print("Hello " + ryan_friend_names[4].title() + ", it's nice to see you again.")
print("Hello " + ryan_friend_names[5].title() + ", it's nice to see you again.")

vehicles = ['Sailboat', 'Tesla', 'Pickup Truck', 'Skateboard']

print("I would love to own a " + vehicles[0].lower() + " and sail around the Hawaiian Islands")
print("I would like to purchase a " + vehicles[1].lower() + " and save money on gasoline.")
print("I will eventually buy an old " + vehicles[2].lower() + " and restore it to its former glory.")
print("I used to " + vehicles[3].lower() + " with my younger brother.")

# update lists with a replaced value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# add elements to a list - append the item to the list, the new element is added to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# you can create an empty list and then add data as you receive it once the program is running as expected. This puts the users in control
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# add a new element to any position using the insert() method, must specify the index of the new element and the value of the new item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove items from a list 
# if you know the position of the item you want to remove you use the del statement
del motorcycles[0]
print(motorcycles)

# removing an item using the pop() method
# pop() removes the last item in a list, but it lets you work with that item after removing it.
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

# if you don't know the position of the value you want to remove you can use the remove() method if you know the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# you can work with a vlue thats being removed from a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# remove only deletes the first occurrence of the value specified. If the value appears more than once in the list you need to use a loop - see chapter 7

dinner_guests = ['Alan Turing', 'Eleanor Roosevelt', 'Barack Obama']
print("I'd like to invite " + dinner_guests[0] + ", " + dinner_guests[1] + ", and " + dinner_guests[2] + " to my dinner party.")
print(dinner_guests[2] + " has informed the host that " + dinner_guests[0] + " can't make it. He sends his apologies.")
del dinner_guests[0]
dinner_guests.append('Hilo Rose Mangum')
print(dinner_guests)
print(dinner_guests[0] + ", " + dinner_guests[1] + ", and " + dinner_guests[2] + " I have found a bigger table and three more guests will be joining us for dinner")
dinner_guests.insert(0, 'Hunter S. Thompson')
dinner_guests.insert(2, 'Joseph Hernandez')
dinner_guests.insert(5, 'Elliott Hamilton')
print(dinner_guests)
print("I want to invite you, " + dinner_guests[0] + " to my dinner party.")
print("I can only invite two people to dinner now, as my new table will not arrive in time")
first_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + first_removed + ".")
second_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + second_removed + ".")
third_removed = dinner_guests.pop(0)
print("I am sorry to have un-invited you, " + third_removed + ".")
fourth_removed = dinner_guests.pop(2)
print("I am sorry to have un-invited you, " + fourth_removed + ".")
print(dinner_guests[0] + " and " + dinner_guests[1] + " you both are still invited to dinner.")
del dinner_guests[0]
del dinner_guests[0]
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

# sorting a list alphabetically is more complicated when all the values are not lowercase.

# print the list in reverse order
cars.reverse()
print(cars)

world_vacations = ["Egypt", "Spain", "Colombia", "Greece", "Indonesia", "Vietnam"]
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

print(f"I am inviting {len(dinner_guests)} guests to dinner.")

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

# if you're getting errors when working with lists, print the list or ask for the len of the list. The list you're working with may be different than you thought.

