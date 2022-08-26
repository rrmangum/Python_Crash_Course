def sandwich_toppings(*toppings):
    """
    Prints the lst of requested toppings
    """
    print("\nYour order consists of the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")