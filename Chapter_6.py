alien_0 ={} # use empty dictionaries when storing user-supplied data or when you write code that generates a large number of key-value pairs automatically
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# modify values
alien_0["color"] = "yellow"
print(alien_0)

# remove key-value pairs
del alien_0["points"]
print(alien_0)

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

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys(): # looping through keys is the default behavior when looping in dictionaries 
    print(name.title())

for name in favorite_languages: # same thing as above
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

# if you want to display key-value pairs in a certain order, you can use the sorted() function
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# values() method returns the values with keys
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# a set is similar to a list except each item in the set must be unique:
for language in set(favorite_languages.values()):
    print(language.title())

rivers = {
    "nile" : "Egypt",
    "Mississippi" : "USA",
    "Rhine" : "Germany",
}

for river, country in rivers.items(): # two different temp variables use .items()
    print(f"The {river} runs through {country}.")

for river in rivers: # default behavior is to pull keys
    print(f"{river.title()}")

for river in rivers.values(): # pull values
    print(f"{river.title()}")

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
        print("Please take the poll")
    else:
        print("Thank you for your response.")

Nesting is storing a set of dictionaries in a list or a list of items as a value in a dictionary

list of aliens in which each alien is a dictionary of information about that alien.
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

# range() automatically generates each alien by telling python how many times we want the loop to repeat
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

# even though they all have the same characteristics, python considers each to be one separate object, allowing us to modify them individually

# if you want to change colors and other characteristics, use a for loop with conditionals:

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
    elif alien['color'] == 'yellow'
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]: # use a slice to the print the first five aliens
    print(alien)
print("...")

it is common practice to store a number of dictionaries in a list when each dictionary contains many kinds of information about one object.

list in a dictionary is useful anytime you want to more than one value to be associated with a single key in a dictionary.
Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
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

You should not nest lists and dictionaries too deeply. If you’re nesting items much deeper than what you see in the preceding examples or you’re working with someone else’s code with significant levels of nesting, most likely a simpler way to solve the problem exists

dictionary in a dictionary gets complicated very quickly

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

nathalie_info = {
    "First Name": "Nathalie",
    "Last Name": "Lozano",
    "Age": "28",
    "City": "Round Rock",
}

conor_info = {
    "First Name": "Conor",
    "Last Name": "Mangum",
    "Age": "28",
    "City": "Norfolk",
}

ian_info = {
    "First Name": "Ian",
    "Last Name": "Mangum",
    "Age": "32",
    "City": "Montgomery"
}

people = [nathalie_info, conor_info, ian_info]

for person in people:
    print(person)

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

favorite_places = {
    "nathalie": ["italy", "mexico", "spain"],
    "ryan": ["mexico", "greece", "korea"],
    "tommy": ["croatia", "czech republic", "italy"],
}

for name, place in favorite_places.items():
    print(name, place)

favorite_numbers = {
    "ryan": ["17", "30"],
    "conor": ["25", "42"],
    "nathalie": ["12", "65"],
}

for name, number in favorite_numbers.items():
    print(name, number)

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
    