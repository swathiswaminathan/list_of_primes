"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """function that does not take any argument, and prints the string 'hello world'"""

    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
##    prints "Hi" followed by the name.
def say_hi(input_name):
    """function that takes a name, and prints 'Hi' followed by the name"""

    print "Hi %s" % (input_name)


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


def print_product(num1, num2):
    """function that takes two integers and prints the product of the two integers"""

    print num1 * num2

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


def repeat_string(input_string, count):
    """function that takes a string and integer and prints string that many times"""

    print input_string * count

# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


def print_sign(num):
    """function that takes a zero and prints whether the number is higher than, lower than or equal to 0"""

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


def is_divisible_by_three(num):
    """function that takes and integer and returns a boolean, depending on whether it is divisible by 3"""

    if num % 3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.
def num_spaces(input_line_string):
    """function that takes a line as a string, and returns the number of spaces"""

    count = 0
    for char in input_line_string:
        if char == " ":
            count += 1

    return count

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


def total_meal_price(meal_price, tip_percentage=0.15):
    """function that takes meal price and tip percentage and returns the total amount paid"""

    total_amount = meal_price + meal_price * tip_percentage
    return total_amount

# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.


def sign_and_parity(num1):
    """function that takes an integer, and returns whether the number is even or odd; and positive or negative"""

    sign_and_parity_list = []
    if num1 > 0:
        sign_and_parity_list.append("Positive")
    else:
        sign_and_parity_list.append("Negative")

    if num1 % 2 == 0:
        sign_and_parity_list.append("Even")
    else:
        sign_and_parity_list.append("Odd")

    return sign_and_parity_list

#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.




###############################################################################

# PART TWO

# 1. Write a function called full_title that takes a name and a job title as
#    parameters, making it so the job title defaults to "Engineer" if a job
#    title is not passed in. Return the person's title and name in one string.

def full_title(name, job_title = "Engineer"):
    """function that takes in name and job title, and returns the parameters as a single string"""
    
    concatenated_string = job_title + " " + name
    return concatenated_string
# 2. Write a function called write_letter that, given a recipient name & job
#    title and a sender name, prints the following letter:
def write_letter(recipient_name, job_title, sender_name):

    """function that takes in recipient name, job title and sender name and prints a message"""
    job_title_and_name = full_title(recipient_name, job_title)
    print "Dear {}, I think you are amazing! Sincerely, {}".format(job_title_and_name, sender_name)

#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    say_hi("Swathi")

    print_product(3,5)

    repeat_string("Balloonicorn",3)

    print_sign(10)

    is_divisible_by_three(9)

    num_spaces("This is a python practice assessment")

    total_meal_price(30, .3)
    total_meal_price(30)
   
    sign_and_parity_list = sign_and_parity(10)
    print sign_and_parity_list

    sign, parity = sign_and_parity_list
    print sign, parity

    full_name_title = full_title("Swathi","Hiker")
    print full_name_title

    write_letter("Iyer","Engineer","Swathi")


    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
