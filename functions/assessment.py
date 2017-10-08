"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def is_hometown(town_name):
    """function that takes a town name and returns True / False depending on whether the town name is user's hometown or not

    >>> is_hometown("San Jose")
    True

    >>> is_hometown("San jose")
    True

    >>> is_hometown("Sunnyvale")
    False

    """
    home_town = "San Jose"
    if town_name.lower() == home_town.lower():
        return True
    else:
        return False


def get_full_name(first_name, last_name):
    """function that takes a first name and last name, and returns the concatenation of the two names

    >>> get_full_name("Swathi", "Iyer")
    'Swathi Iyer'

   """

    full_name = "{} {}".format(first_name, last_name)
    return full_name


def print_message(first_name, last_name, home_town):
    """function that takes in first name, last name, hometown and prints a message

    >>> print_message("Swathi","Iyer","San Jose")
    Hi Swathi Iyer,we're from the same place!

    >>> print_message("Swathi","Iyer","Sunnyvale")
    Hi Swathi Iyer, I'd like to visit Sunnyvale!

    """
    full_name = get_full_name(first_name, last_name)
    if is_hometown(home_town):
        print "Hi {},we're from the same place!".format(full_name)
    else:
        print "Hi {}, I'd like to visit {}!".format(full_name, home_town)




###############################################################################




# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees


def is_berry(fruit):
    """Determines if fruit is a berry, return True if a berry, otherwise False

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    if fruit.lower() == "strawberry" or fruit.lower() == "raspberry" or fruit.lower() == "blackberry" or fruit.lower() == "currant":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit, returns cost depending on whether fruit is a berry or not

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    if is_berry(fruit):
        return 0

    return 5


def append_to_list(fruit_list, single_fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']

    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> append_to_list(fruits, 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']
    >>> fruits
    ['banana', 'apple', 'blackberry']

    """
    new_fruits_list = []
    for fruit in fruit_list:
        new_fruits_list.append(fruit)
    new_fruits_list.append(single_fruit)

    return new_fruits_list


def calculate_price(base_price, state_abbr, tax_percent=.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    #defining cost, which is the basic cost after adding basic price and tax
    cost = base_price + (base_price * tax_percent)
    additional_fee = 0

    if state_abbr == "CA":
        additional_fee = cost * (.03)
    elif state_abbr == "PA":
        additional_fee = 2
    elif state_abbr == "MA":
        if base_price <= 100:
            additional_fee = 1
        else:
            additional_fee = 3

    total_cost = cost + additional_fee
    return total_cost



###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

def print_appended_list(alist, *args):
    """function to append any number of strings to a given list and return the appended list

    >>> print_appended_list([1, 2, 3], "addition", "keyword","swathi", "not bad")
    [1, 2, 3, 'addition', 'keyword', 'swathi', 'not bad']

    >>> print_appended_list([1, 2, 3])
    [1, 2, 3]
    """
    for arg in args:
        alist.append(arg)

    return alist

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:


def outer(word):
    """function that takes a word and prints the word and three times the word in form of a tuple

    >>> outer("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """
    def inner_word(word):
        return word * 3

    multiple_word = inner_word(word)
    return (word, multiple_word)



#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
