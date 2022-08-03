# use empty dictionaries when storing user-supplied data or when you write 
# code that generates a large number of key-value pairs automatically
alien_0 ={} 
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# modify values
alien_0["color"] = "yellow"
print(alien_0)

# remove key-value pairs
del alien_0["points"]
print(alien_0)

# Exercise 6-1 Person
'''
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary
'''

nathalie_info = {
    "First Name": "Nathalie",
    "Last Name": "Lozano",
    "Age": "28",
    "City": "Round Rock",
}
print(nathalie_info["First Name"])
print(nathalie_info["Last Name"])
print(nathalie_info["Age"])
print(nathalie_info["City"])

# Exercise 6-2 Favorite Numbers
'''
Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a 
favorite number for each person, and store each as a value in your dictionary. 
Print each person's name and their favorite number. For even more fun, poll a 
few friends and get some actual data for your program.
'''
favorite_numbers = {
    "Ryan": "17",
    "Nathalie": "12",
    "Elliott": "28",
    "Ian": "29",
    "Conor": "25",
}
for key, value in favorite_numbers.items():
    print(key, value)

# Exercise 6-3 Glossary
'''
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.

-> Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.

-> Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''
programming_words = {
    "list": "data container",
    "append": "add something to something",
    "string": "data type",
    "del": "delete something",
    "dictionary": "data container",
}
print(programming_words)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through keys is the default behavior when looping in dictionaries 
for name in favorite_languages.keys(): 
    print(name.title())

for name in favorite_languages: # same thing as above
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is" 
          "{favorite_languages[name].title()}!")

# if you want to display key-value pairs in a certain order, you can 
# use the sorted() function
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# values() method returns the values with keys
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# a set is similar to a list except each item in the set must be unique:
for language in set(favorite_languages.values()):
    print(language.title())

# Exercise 6-4 Glossary 2
'''
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary's keys and values.
When you're sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
'''
programming_words = {
    "list": "data container",
    "append": "add something to something",
    "string": "data type",
    "del": "delete something",
    "dictionary": "data container",
    ".loc": "locate a series within a pandas dataframe",
    ".describe": "provides summary statistics in pandas",
    ".plot": "plots data in various visual representations",
    "import": "use functions from other python files",
    "pd.read_csv": "read a csv file using pandas",
}

for word, definition in programming_words.items():
    print(f"{word}: {definition}")

# Exercise 6-5 Rivers
'''
Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.

-> Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.

-> Use a loop to print the name of each river included in the dictionary.

-> Use a loop to print the name of each country included in the dictionary.
'''
rivers = {
    "Nile" : "Egypt",
    "Mississippi" : "USA",
    "Rhine" : "Germany",
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

for river in rivers: # default behavior is to pull keys
    print(f"{river.title()}")

for river in rivers.values(): # pull values
    print(f"{river.title()}")

# Exercise 6-6 Polling
'''
Use the code in favorite_languages.py (page 104).

-> Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.

-> Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = [
    'jen',
    'nathalie',
    'ryan',
    'edward',
    'ian',
    'conor'
]

for taker in poll_takers:
    if not taker in favorite_languages:
        print(f"{taker.title()}, Please take the poll")
    else:
        print(f"{taker.title()}, Thank you for your response.")

# Nesting is storing a set of dictionaries in a list or a list of 
# items as a value in a dictionary

# list of aliens in which each alien is a dictionary of 
# information about that alien.
alien_0 = {
    'color': 'green', 
    'points': 5
}
alien_1 = {
    'color': 'yellow', 
    'points': 10
}
alien_2 = {
    'color': 'red', 
    'points': 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# range() automatically generates each alien by telling python how many 
# times we want the loop to repeat
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # add the new_alien to the list aliens

# show first 5 aliens
for alien in aliens[:5]: # use a slice to the print the first five aliens
    print(alien)
print("...")

# show how many aliens have been created. by printing the length of the list
print(f"Total number of aliens: {str(len(aliens))}")

# even though they all have the same characteristics, python considers each 
# to be one separate object, allowing us to modify them individually

# if you want to change colors and other characteristics, use a for 
# loop with conditionals:

for alien in aliens[0:3]: # use a slice to modify only the first three aliens.
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]: # use a slice to the print the first five aliens
    print(alien)
print("...")

# conduct multiple changes at once

for alien in aliens[0:3]: # use a slice to modify only the first three aliens.
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]: # use a slice to the print the first five aliens
    print(alien)
print("...")

# it is common practice to store a number of dictionaries in a list when each 
# dictionary contains many kinds of information about one object.

# list in a dictionary is useful anytime you want to more than one value to be 
# associated with a single key in a dictionary.
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# You should not nest lists and dictionaries too deeply. If you’re nesting 
# items much deeper than what you see in the preceding examples or you’re 
# working with someone else’s code with significant levels of nesting, most 
# likely a simpler way to solve the problem exists

# dictionary in a dictionary gets complicated very quickly

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
 }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Exercise 6-7 People
'''
Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
'''
nathalie = {
    "First Name": "Nathalie",
    "Last Name": "Lozano",
    "Age": "28",
    "City": "Round Rock",
}

conor = {
    "First Name": "Conor",
    "Last Name": "Mangum",
    "Age": "28",
    "City": "Norfolk",
}

ian = {
    "First Name": "Ian",
    "Last Name": "Mangum",
    "Age": "32",
    "City": "Montgomery"
}

people = [nathalie, conor, ian]

for person in people:
    print(person)

# Exercise 6-8 Pets
'''
Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner's
name. Store these dictionaries in a list called pets. Next, loop through your 
list and as you do print everything you know about each pet.
'''
hilo = {
    "animal type": "Dalmatian",
    "owner's name": "Ryan and Nathalie",
}

cosmo = {
    "animal type:": "Australian Shepard",
    "owner's name": "Josh",
}

hank = {
    "animal type": "Labradoodle",
    "owner's name": "Pat and Charlotte",
}

pets = [hilo, cosmo, hank]

for pet in pets:
    print(pet)

# Exercise 6-9 Favorite Places
'''
Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some 
friends to name a few of their favorite places. Loop through the dictionary, 
and print each person's name and their favorite places.
'''
favorite_places = {
    "nathalie": ["italy", "mexico", "spain"],
    "ryan": ["mexico", "greece", "korea"],
    "tommy": ["croatia", "czech republic", "italy"],
}

for name, place in favorite_places.items():
    print(name, place)

# Exercise 6-10 Favorite Numbers
'''
Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person's
name along with their favorite numbers.
'''
favorite_numbers = {
    "ryan": ["17", "30"],
    "conor": ["25", "42"],
    "nathalie": ["12", "65"],
}

for name, number in favorite_numbers.items():
    print(name, number)

# Exercise 6-11 Cities
'''
Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one 
fact about that city. The keys for each city's dictionary should be something 
like country, population, and fact. Print the name of each city and all of the 
information you have stored about it.
'''
cities = {
    "Austin": {
        "State": "Texas",
        "Population": "1,000,000", 
        "Fact": "It's weird"
    },
    "Montgomery": {
        "State": "Alabama", 
        "Population": "200,000", 
        "Fact": "Civil Rights Movement"
    },
    "Los Angeles": {
        "State": "California", 
        "Population": "10,000,000", 
        "Fact": "Hollywood"
    },
}

for city, city_info in cities.items():
    print(f"\n{city} is a fun place to live! Here are some facts:")
    print(f"{city} is in {city_info['State']}.")
    print(f"Its population is {city_info['Population']}.")
    print(f"Here is a fun fact: {city_info['Fact']}.")    