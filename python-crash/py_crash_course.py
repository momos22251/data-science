# formating text: you can indicate the name of the variable within the string
first_name = "mohamed"
last_name = "mostafa"
print("my first name is {one}, and my last name is {two}".format(one=first_name, two=last_name))

# appending lists:
lisa = []
for i in first_name:
    lisa.append(i)
print(lisa)
print(lisa[:])
print(lisa[:3])
print(lisa[3:])
# nested lists
lisa.append([1, 2, 3, 4])
lisa[7][2]


# Dictionaries
dic = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': ['value4', 'value5', 'value5'],
    'key5': {
        'nested_key':{
            'inner_key':[0,1,2,3,4,5,6,7,8],
        }
    }
}

dic['key5']['nested_key']['inner_key'][5]
dic['key4'] = 'changed_value'
dic.items() # all the keys and their corrsponding values
dic.keys() # only the keys
dic.values() # only the vlaues



# Tuples: the main difference between the tuples and lists
# is that you can reassign the items within a list but cant do that with a tuple
# so we use the tuples to make sure that the user can not change the items inside a sequence
# of objects <list is mutable and tuple is inmutable>   
tuba = (1, 2, 3 , 'mohamed', 'mostafa')
# try:
#     tuba[0] = 'reassigned value'
# except TypeError:
#     print("Hey there, you can not reassign the items within a tuple")

# Sets: returns a set of only the unique elements <no repeats>
setty = {1,2,1,5,3,6,4,8,3,1,5,1,1,1,5,5,5,9,9,8,9,3}
setty
setty.add(101)
# also you can create a set from a list to return a collection of the unique elements
lita = [1,2,1,5,3,6,4,8,3,1,5,1,1,1,5,5,5,9,9,8,9,3]
set(lita)


# COMPARISON OPERATORS : == , > , < , >= , <= , != 
# LOGICAL OPERAETORS : and , or , !
(1 < 2) and (2 > 3) # the two conditons should be True or it will give False
(1 < 2) or (2 > 3) # at least if one is True it will give True
True or False
False or False
True and True
False and True
True and False or True


# FOR LOOP
name = 'mohamed mostafa'
name = name.strip().split()
i = 1
for item in name:
    print("the name number {} is {}".format(i, item))
    i = i+1

for i in range(6):
    print(i)

list(range(11))


# LIST COMPERHENSION : saves you time instead of using for loop
out = []
for num in range(11):
    out.append(num**2)

# list comp = [what you want<out.append(i**2)> for <i in range(11)>]
out = [num**2 for num in range(11)]


# FUNCTIONS
def even_odd(number):
    """
    This is a function decides if a given number
    is odd or even.
    """
    if number%2 == 0:
        return "the number {} is even".format(number)
    else:
        return "the number {} is odd".format(number)


print(even_odd(5))
print(even_odd(4))


# MAP and FILTER functions

def times2(number):
    """
    this function returns a number multiplied by 2
    """
    return number*2

reta = [1,2,3,4,5]
# if i want to apply "times2" function to all the values inside the "reta" list
# 1- you can use for loop and append the results to another list
new_reta = []
for i in reta:
    new_reta.append(times2(i))
print(new_reta)

# 2- using 'map()' function map(function_to_be_applied, list_of_items_to+be_applied_on)
mapping_reta = map(times2, reta) # this gives you a function
modern_reta = list(map(times2, reta)) # taking the values into a list


# LAMBDA expression: to create simple functions instead of (def) defining a function for every thing
def power2(number): return number**2 # this is how to write simple functions on a single line.
power2(10)
#  lambda expression mimics the previous expression but with removing the keywords like (def, return)
power = lambda number:number**2
power(10)

# and you can use the 'lambda' expression with 'map()'
lazy = [2,3,5,12,64]
lazy_powered2 = list(map(lambda number:number**2, lazy)) # this is gonna return a 'lazy' list
# with all the items powered by two 2


# FILTER: filter out elements from a list or a sequence

# lambda expression takes every number and returns True or False and pass it to iterable object
# and when you call a list function on it it will grab and return only the Ture values
# (according to the lambda conditional function) 
lazy_even = list(filter(lambda number: number%2 == 0, lazy)) # this returns all the even a number 
lazy_odd = list(filter(lambda number: number%2 != 0, lazy)) # this returns all the odd numbers

print('lazy even numbers are : ', lazy_even)
print('lazy odd numbers are : ', lazy_odd)


# STRINGS:
s = 'Hello My Name Is Mohamed'
s.split()
s.upper()
s.lower()

# the split method is very important in string analysis
# for example in twitter hastags
tweet = 'this is a twitter #hastag #anotherHastag' 
tweet.split('#')[1]


# Lists: removing items from a list
lst = [5,2,1,5,13,26,64,8,484,54,51,2,9]
lst.pop() # pop and returns the last item in a list
lst # the last item has been removed after .pop()
first_item = lst.pop(0) # this will remove the item with index=0
lst
first_item


# IN operator: check is something is inside a list
'x' in ['x', 'y', 'z'] # this is gonna return True as x is in the list
'x' in ['y', 'z'] # this is gonna return False as x is not in the list


# TUPLE UNPACKING
x = [(1,2),(3,4),(5,6),(7,8)] # this is a list of tubles that you can access by index
x[3] # this will return the last tuple of the list

for item in x:
    """
    this is gonna print all the tuples
    """
    print(item)

# tuple unpacking
for a,b in x:
    """
    this returns the first item in each tuple
    """
    print(a)

