# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

def tax_function(cost, state, tax=1.05): # defaulting tax parameter
    if state != 'CA': # creating if statement to not include california to use default tax
        after_tax_cost = tax * cost # calculating cost
        return after_tax_cost
    else:
        after_tax_cost = 1.07 * cost  # calculating cost
        return after_tax_cost

print tax_function(50,'CA') #calling function! defined each parameter to avoid weird messages in console 


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is at "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################


# PART TWO
#--------------1.a-------------------#
def is_berry(fruit): # defining function and parameters
    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True # only returning true if the fruit entered is the ones listed
    else:
        return False # returning false if string entered doesn't contain accepted fruit name

print is_berry('banana')

#-------------end of 1.a-------------#

#--------------1.b-------------------#
def shipping_cost(fruit):
    if is_berry(fruit) == True is True: # calling previous funciton
        return '0' # returning 0 if is_berry(fruit) returned True
    else:
        return '5' # returning 5 if is_berry(fruit) returned False

print shipping_cost('strawberry')

#-------------end of 1.b-------------#

#--------------2.a-------------------#
def home_town(home):
    my_home = 'Benicia' # defining MY HOME TOWN!
    if my_home != home: # comparing the two and printing out false if not true
        return False
    else:
        return True

print home_town('Vallejo')

#-------------end of 2.a-------------#

#--------------2.b-------------------#

def full_name(first,last): #defining function
    name = first + ' ' + last #concatenation - ooOOo need to get this word down
    return name # return the concatenation of first and last

print full_name('Sanchita', 'Saxena')

#-------------end of 2.b-------------#

#--------------2.c-------------------#

def hometown_greeting(home,first,last):
    their_name = full_name(first,last) #defining the name by calling previous function
    if home_town(home) == True is True:
        return "Hi, %r, we're from the same place!" % their_name # printing if true
    else:
        return "Hi, %r, where are you from?" % their_name # printing if False

print hometown_greeting('New York', 'Forrest', 'Chamberlain') 

#-------------end of 2.c-------------#


# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################

# PART THREE

#--------------1------------------#

def incriment(y, x=1): # takes x and y but x is defaulted to 1
    def add(): #nested funciton
        return x + y #adding the incriment
    return add() # calling the nested function

print incriment(5) # printing

#--------------2-------------------#

addfive = incriment(y=0, x=5) # increment changed to 5
print addfive # check 
addone = incriment(y=5) # increment defaulted, y changed to 5
print addone # check 
addtwenty = incriment(y=20) #increment defaulted, y changes to 20
print addtwenty # check 

#--------------3-------------------#

def create_list(num,a_list): # parameters 
    a_list.append(num) #adding the number
    return a_list #returning the new a_list

print create_list(5,[1,2,3,4]) # calling/checking

