from printing_functions import print_models, show_completed_models
# import sandwich_toppings
# from sandwich_toppings import sandwich_toppings
# from sandwich_toppings import sandwich_toppings as st
# import sandwich_toppings as st
from sandwich_toppings import *


# Exercise 8-15 Printing Models
"""
Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.
"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Exercise 8-16 Imports
"""
Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
"""

# import sandwich_toppings 
# sandwich_toppings.sandwich_toppings('bacon', 'lettuce', 'tomato')

# from sandwich_toppings import sandwich_toppings
# sandwich_toppings('bacon', 'lettuce', 'tomato')

# from sandwich_toppings import sandwich_toppings as st
# st('bacon', 'lettuce', 'tomato')

# import sandwich_toppings as st
# st.sandwich_toppings('bacon', 'lettuce', 'tomato')

# from sandwich_toppings import *
sandwich_toppings('bacon', 'lettuce', 'tomato')
