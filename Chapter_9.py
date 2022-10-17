# # Chapter 9 Classes

# # Creating and Using a Class
# # To create a class think of the topic and what is common to that topic. 
# # With a Dog class we can recognize that most dogs have a name, an age, know how
# # to sit, and know how to roll over.
# # The class tells Python how to make an object representing a dog. 
# # We can then use the class to make individual instances each representing one
# # specific dog

# # Define the class. Capitilzed names refer to classes in Python. () is empty
# # because we're creating this class from scratch.
# class Dog:
#     # docstring describing what the class does
#     """A simple attempt to model a dog"""

#     # A function that's part of a class is a method. Everything about functions
#     # applies to methods as well, the only difference for now is the way you 
#     # call methods. __init__() method is a special method Python runs
#     # automatically whenever we create anew instance based on the Dog class.
#     # the syntax helps prevent Python's default method names from conflicting
#     # with your method names

#     # self parameter is required in the method definition, and it must come
#     # first before the other parameters. It must be included in the definition 
#     # becuase when Python calles the method later (to create an instance of Dog)
#     # the method call will automatically pass the self argument. Every method
#     # call associated with a class automatically passes self, which is a
#     # reference to the instance itself. It gives the individual instance access
#     # to the attributes and methods in the class.

#     # When we make an instance of Dog, Python will call the __initi__() method
#     # from the dog class. We'll pass Dog() a name and an age as arguments, self
#     # is passed automatically, so we don't need to pass it.
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         # Any variable prefixed with self is available to every method in the
#         # class and we can access these variables through any instance created
#         # from the class.

#         # take the value stored in the parameter name and stores it in the
#         # variable name, which is then attached to the instance being created.
#         # These variables accesed through instances are called attributes 
#         self.name = name
#         self.age = age
    
#     # Two other methods that don't need additional information like a name or
#     # age, we can just define them to have on parameter, self. Instances created
#     # later have access to these methods.
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name.title()} is now sitting.")
        
#     def roll_over(self):
#         """Simulate a dog rolling over in reponse to a command"""
#         print(f"{self.name.title()} rolled over!")

# # Think of a class as a set of instructions for how to make an instance. The
# # class Dog is a set of instructions that tells Ptyhon how to make individual
# # instances representing sepecific dogs.

# # Tell Python to create a dog named Hilo and is 2 years old. When Python reads
# # this line, it calles the __init__() method in Dog with the arguments 'Hilo'
# # and 2. The __init__() method creates an instance represnting this particular
# # dog and sets the name and age atrributes using the values provided.
# # __init__() method does not have a return return statement, but Python
# # automatically returns an instance represnting this dog. The instance is stored
# # in the variable my_dog.
# my_dog = Dog('Hilo', 2)

# # To access attritutes of an instance you use dot notation.The syntax
# # demonstrates how Python finds an attirbutes's value. Python looks at the 
# # instance my_dog and then finds the attribute name associated with my_dog.
# # This is the same attribute referred to as self.name in the class Dog.
# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")

# # Calling Methods

# # After creating an instance from the class Dog, use dot notation to call any
# # method defined in Dog

# my_dog.sit()
# my_dog.roll_over()

# # You can create as many instances (objects) from a class as you need
# your_dog = Dog('Max', 1)

# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"Your dog's name is {your_dog.name.title()}.")

# your_dog.sit()

# # Exercise 9-1 Restaurant
# """
# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open. Make an instance called restaurant 
# from your class. Print the two attributes individually, and then call both methods.
# """

# class Restaurant:
#     """
#     This class organizes data and provides functions to describe restaurants
#     """

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """
#         This method describes the restaurant by printing the name and the cuisine
#         """
#         print(f"The restaurant's name is {self.restaurant_name}.")
#         print(f"The restaurant serves {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         """
#         This method opens the restaurant
#         """

#         print(f"The restaurant is open!")

# restaurant = Restaurant('Formosa', 'Chinese')

# # Print the attributes
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# # Call the methods
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # Exercise 9-2 Three Restaurants
# """
# Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
# """

# mercado = Restaurant('Mercado', 'Mexican')
# formosa = Restaurant('Formosa', 'Chinese')
# blackbird = Restaurant('Blackbird', 'Pizza')

# mercado.describe_restaurant()
# formosa.describe_restaurant()
# blackbird.describe_restaurant()

# # Exercise 9-3 Users
# """
# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user's information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
# """

# class User:

#     def __init__(self, first_name, last_name, user_name, email):
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.user_name = user_name
#         self.email = email
    
#     def describe_user(self):
#         print(f"Here is this user's information: \nFirst Name: {self.first_name}, \nLast Name: {self.last_name}, \nUsername: {self.user_name}, \nEmail: {self.email}")

#     def greet_user(self):
#         print(f"Hello {self.user_name}, what would you like to do today?")

# rydog = User('Ryan', 'Mangum', 'rydog', 'rydog@gmail.com')
# natty = User('Nathalie', 'Lozano', 'natty', 'natty@gmail.com')
# conman = User('Conor', 'Mangum', 'conman', 'conman@gmail.com')

# rydog.describe_user()
# rydog.greet_user()

# natty.describe_user()
# natty.greet_user()

# conman.describe_user()
# conman.greet_user()

# class Car:
#     """
#     A simple attempt to represent a car."""

#     # init method takes in parameters and stores them as attributes
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """
#         Return a neatly formatted descriptive name.
#         """
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """
#         Print a statement showing the car's mileage.
#         """
#         print(f"This car has {self.odometer_reading} miles on it.")

#     # modify an attribute's value through a method
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     # sometimes you'll want to increment an attributes value by a certain amount rather than set an
#     # entirely new value
#     def increment_odometer(self, miles):
#         """
#         Add the given amount to the odometer reading.
#         """
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("You can't subtract miles from the odometer!")


# # new instance of the car class stored as a variable
# my_new_car = Car('audi', 'a4', '2016')

# # method call to describe the car
# print(my_new_car.get_descriptive_name())

# my_new_car.read_odometer()

# # modify attributes through the attribute directly through an instance
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# # modify attributes through a method
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# # sometimes you'll want to increment an attributes value by a certain amount rather than set an
# # entirely new value
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-100)
# my_used_car.read_odometer()

# # Exercise 9-4 Number Served
# """
# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who've been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a day of business.
# """
# class Restaurant:
#     """
#     This class organizes data and provides functions to describe restaurants
#     """

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 5

#     def describe_restaurant(self):
#         """
#         This method describes the restaurant by printing the name and the cuisine
#         """
#         print(f"The restaurant's name is {self.restaurant_name}.")
#         print(f"The restaurant serves {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         """
#         This method opens the restaurant
#         """

#         print(f"The restaurant is open!")

#     def set_number_served(self, number_served):
#         """
#         This method sets the number served.
#         """
#         self.number_served = number_served

#     def increment_number_served(self, new_customers):
#         """
#         This method adds customers served to the restaurant's total.
#         """
#         self.number_served += new_customers

# restaurant = Restaurant('Formosa', 'Chinese')

# print(restaurant.number_served)
# restaurant.set_number_served(1000)
# print(restaurant.number_served)

# restaurant.increment_number_served(55)
# print(restaurant.number_served)

# # Exercise 9-5
# """
# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
# """
# class User:

#     def __init__(self, first_name, last_name, user_name, email):
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.user_name = user_name
#         self.email = email
#         self.login_attempts = 0
    
#     def describe_user(self):
#         print(f"Here is this user's information: \nFirst Name: {self.first_name}, \nLast Name: {self.last_name}, \nUsername: {self.user_name}, \nEmail: {self.email}")

#     def greet_user(self):
#         print(f"Hello {self.user_name}, what would you like to do today?")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

# rydog = User('Ryan', 'Mangum', 'rydog', 'rydog@gmail.com')

# rydog.increment_login_attempts()
# rydog.increment_login_attempts()
# rydog.increment_login_attempts()
# rydog.increment_login_attempts()

# print(rydog.login_attempts)

# rydog.reset_login_attempts()
# print(rydog.login_attempts)

# Use inheritance when you're writing a specialized version of another class you wrote
# When one class inherits from another. it automaticall takes on all the attributes and methods
# of the first class. Original class is called the parent class and the specialized class is
# called the child class.
