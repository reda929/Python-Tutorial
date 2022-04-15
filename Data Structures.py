#########
# LISTS #
#########

# lists are mutable ordered data structures
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for i, m in enumerate (months):
    print (f'{i:2d}: \t{m}')
#  0: 	January
#  1: 	February
#  2: 	March
#  3: 	April
#  4: 	May
#  5: 	June
#  6: 	July
#  7: 	August
#  8: 	September
#  9: 	October
# 10: 	November
# 11: 	December

q3 = months[6:9]
print (q3)  # [ 'July', 'August', 'September']

first_half = months[:6]
print (first_half)  # ['January', 'February', 'March', 'April', 'May', 'June']
second_half = months[6:]
print (second_half)  # ['July', 'August', 'September', 'October', 'November', 'December']

print (len (months))  # 12
print ('in' in 'this is a string') # True
print ('isa' in 'this is a string') # False
print (5 not in [1, 2, 3, 4, 6]) # True
print (5 in [1, 2, 3, 4, 6]) # False
list = ['d', 'a', 'b', 'c', 'a', 'b']

# list.count(x): returns the number of occurrences of x in the list
print (list.count ('a'))  # 2
print (list.count ('g'))  # 0

# list.index(x[, start[, end]]): returns the first item whose value is equal to x in the list (starting index is optional, so is end index)
print (list.index ('b'))  # 2
print (list.index ('b', 2))  # 2
print (list.index ('b', 3))  # 5

# list.copy(): returns a unique shallow copy of the list
list_copy = list.copy ()
print (id (list))  # 1900515497728
print (id (list_copy))  # 1900515781568
print (list_copy)  # ['d', 'a', 'b', 'c', 'a', 'b']

# list.sort(*, key=None, reverse=False): sorts the items of the list in place
# not all data can be sorted or compared, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types
# also, there are some types that don’t have a defined ordering relation, 3+4j < 5+7j isn’t a valid comparison for example
list.sort ()
print (list)  # ['a', 'a', 'b', 'b', 'c', 'd']

# list.reverse(): reverses the elements in the list
list.reverse ()
print (list)  # ['d', 'c', 'b', 'b', 'a', 'a']

# list.append(x): adds an item to the end of the list
list.append ('c')
print (list)  # ['d', 'c', 'b', 'b', 'a', 'a', 'c']

# list.extend(iterable): adds an iterable's items to the end of the list
num_list = [10, 20, 30]
num_list.extend (range (10, 30, 3))
print (num_list)  # [10, 20, 30, 10, 13, 16, 19, 22, 25, 28]

# list.insert(i, x): inserts an item x at index i
num_list.insert (2, 44)
print (num_list)  # [10, 20, 44, 30, 10, 13, 16, 19, 22, 25, 28]

# list.remove(x): removes the first item whose value is equal to x, but raises a ValueError if such item does not exist in the list
list.remove ('c')
print (list)  # ['d', 'b', 'b', 'a', 'a', 'c']

# list[start:end] = replacement_list: replaces the items at indices start inc to end exc with replacement_list
# replacement_list can be empty, which means removing those elements

list_copy = list.copy ()
list_copy[2:4] = ['green', 'blue']
print (list_copy)  # ['d', 'b', 'green', 'blue', 'a', 'c']
list_copy[1:3] = []
print (list_copy)  # ['d', 'blue', 'a', 'c']

# list.pop([i]): removes the item at the index i, and returns it. default index is len(a)-1, i.e., a.pop() removes the last item from the list, and returns it
print (list.pop ())  # c
print (list)  # ['d', 'b', 'b', 'a', 'a']
print (list.pop (2))  # b
print (list)  # ['d', 'b', 'a', 'a']

# list.clear(): removes all items from the list. equivalent to del a[:]
# the returned index is absoulte, not relative to the start index
list.clear ()
print (list)  # []

# list([iterable]): returns a list populated with the iterable's elements (keys only in dictionariesdictionary) (in insertion order if iterable is ordered)
print (list ({'key 1': 111, 'key 2': 222}))  # ['key 2', 'key 3']


#######################
# List Comprehensions #
#######################

squares = []
for x in range (10):
    squares.append (x ** 2)
print (squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# equivalent to:
squares = [x ** 2 for x in range (10)]
# list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result is a new list resulting from evaluating the expression
print ([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# (1, 3), (1, 3), (1, 3),
# (2, 1), (2, 1), (2, 1),
# (3, 4), (3, 4), (3, 4)
#
# (1, 3),         (1, 4),
# (2, 3), (2, 1), (2, 4),
#         (3, 1), (3, 4)

# which is equivalent to:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append ((x, y))
print (combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print ([x * 2 for x in vec])  # [-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
print ([x for x in vec if x >= 0])  # [0, 2, 4]
# apply a function to all the elements
print ([abs (x) for x in vec])  # [4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print ([weapon.strip () for weapon in freshfruit])  # ['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square). tuple must be parenthesized, otherwise an error is raised
print ([(x, x ** 2) for x in range (6)])  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# multiple for statements
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print ([l2 for l1 in vec for l2 in l1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions can contain complex expressions and nested functions:
from math import pi


[str (round (pi, i)) for i in range (1, 6)]  # ['3.1', '3.14', '3.142', '3.1416', '3.14159']

##############################
# Nested List Comprehensions #
##############################
# first expression in list comprehension can be any arbitrary expression, including another list comprehension.
# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ]
# The following list comprehension will transpose rows and columns:
print ([[row[i] for row in matrix] for i in range (4)])  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# which is equivalent to:
transposed = []
for i in range (4):
    transposed.append ([row[i] for row in matrix])
print (transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# which is equivalent to:
transposed = []
for i in range (4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append (row[i])
    transposed.append (transposed_row)
print (transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:
print (list (zip (*matrix)))  # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

##########
# NOTES: #
##########
# lists' appends and pops from the beginning are slow
# lists are not efficient for queues
# list.pop()
# 0 -> 1 -> 2 -> 3
#      1 -> 2 -> 3
# X <- 1           ... step 1
# 1   X <- 2       ... step 2
# 1   2    X <- 3  ... step 3
# 1   2    3       ... end
# same for list.append() but by adding a node
# but appends and pops from the end of list are fast, and can see now why

# for that, collections.deque was designed for fast appends and pops from both ends
# from collections import deque
# queue = deque (["Eric", "John", "Michael"])
# queue.append ("Terry")  # Terry arrives
# print (queue)
# queue.append ("Graham")  # Graham arrives
# print (queue)
# queue.popleft ()  # 'Eric'
# print (queue)
# queue.popleft ()  # 'John'
# print (queue)  # deque(['Michael', 'Terry', 'Graham'])

##########
# TUPLES #
##########

# tuples are immutable ordered data structures, i.e., you can't add and remove items from tuples, or sort them in place
# usually used to store related pieces of information
singleton = 'hello',  # <-- note trailing comma
d = 1
e = 2
f = 3
# next sentence:
a, b, c = d, e, f
# means:
# 1- packing a, b, c into (a, b, c) tuple, and packing = d, e, f into (d, e, f) tuple
# 2- unpacking every first element in first tuple first element in second tuple
# parentheses are optional, same as:
(a, b, c) = (d, e, f)

nums = d, e, f
# means packing = d, e, f into (d, e, f) tuple, then assign that tuple to variable nums
for i in range (len (nums)):
    print (f'nums[{i}]: {nums[i]}')
# nums[0]: 1
# nums[1]: 2
# nums[2]: 3

# tuples do not support comprehensions directly:
# print ((x: x ** 2 for x in (2, 4, 6))) # invalid syntax
#  using indirect approaches for comprehensions:
print (tuple ([x ** 2 for x in (2, 4, 6)]))  # (4, 16, 36)

########
# SETS #
########
# set is a mutable, unordered (there is no 'first element' or 'last element') data structure with unique elements (no duplicates when initiated from elements like a list)
# operations on sets are much faster than operations on other data structures
# supports mathematical operations like union, intersection, difference, and symmetric difference.

nums = {'one', 'two', 'three', 'one'}
unique_nums = set (nums)
# printing result may vary between executions
print (unique_nums)  # {'two', 'one', 'three'}
print ('one' in unique_nums)  # True

# add(): adds an element
nums.add ('five')
print (nums)
# pop(): returns a random element (every execution time) and removes it
print (nums.pop ())
print (nums)

# mathematical operations
a = set ('oneo')
b = set ('twot')
print ("a = set ('oneo'): ", a)  # a = set ('oneo'):  {'e', 'o', 'n'}
print ("b = set ('twot'): ", b)  # b = set ('twot'):  {'t', 'o', 'w'}
print ('unique letters in a: ', a)  # unique letters in a:  {'e', 'o', 'n'}
print ('unique letters in a but not in b: ', a - b)  # unique letters in a but not in b:  {'e', 'n'}
print ('unique letters in a or b (notice \'uniqueness\' is applied after merging, \'o\' is omitted): ', a | b)  # unique letters in a or b (notice 'uniqueness' is applied after merging, 'o' is omitted):  {'e', 'n', 'o', 'w', 't'}
print ('unique letters in both a and b: ', a & b)  # unique letters in both a and b:  {'o'}
print ('unique letters in a but not both: ', a ^ b)  # unique letters in a but not both:  {'t', 'e', 'w', 'n'}

# set comprehensions are also supported:
a = {x for x in 'twenty' if x not in 'two'}
print (a)  # {'e', 'y', 'n'}

################
# DICTIONARIES #
################
# dictionary is a mutable data structure mapping unique keys to values
# can have keys of any immutable type, like integers or tuples, not just strings. Keys can even be of different types

# to see if a key is in the dictionary, use in
dictionary = {'key 1': 111, 'key 2': 222}
print (dictionary)  # {'key 1': 111, 'key 2': 222}
# equivalent to:
dictionary = dict ([('key 1', 111), ('key 2', 222)])
print (dictionary)  # {'key 1': 111, 'key 2': 222}

dictionary['key 3'] = 333
print (dictionary)  # {'key 1': 111, 'key 2': 222, 'key 3': 333}
print ("dictionary['key 2']: ", dictionary.get ('key 2'))  # 222
# same as the next, but will raise an error if key does not exist in the dictionary:
print ("dictionary['key 2']: ", dictionary['key 2'])  # 222

del dictionary['key 1']
print (dictionary)  # {'key 2': 222, 'key 3': 333}

print (list (dictionary))  # ['key 2', 'key 3']
print (sorted (dictionary, reverse = True))  # ['key 3', 'key 2']
print ("'key 1' in dictionary: ", 'key 1' in dictionary)  # 'key 1' in dictionary: False
print ("'key 5' not in dictionary: ", 'key 5' not in dictionary)  # 'key 5' not in dictionary: True

###############################
# Dictionaries Comprehensions #
###############################
print ({x: x ** 2 for x in (2, 4, 6)})  # {2: 4, 4: 16, 6: 36}
# when keys are strings, keyword arguments can be used:
print (dict (key_1 = 111, key_2 = 222, key_3 = 333))  # {'key_1': 111, 'key_2': 222, 'key_3': 333}

# looping dictionaries for keys and values
# items(): returns a new view of the dictionary’s items ((key, value) pairs)
# keys(): return a new view of the dictionary’s keys
# values(): returns a new view of the dictionary’s values
dictionary = {'key 1': 'value 1', 'key 2': 'value 1'}
print ('dictionary = ')
for key, value in dictionary.items ():
    print (key, value)
# key 1 value 1
# key 2 value 1

# Compound Data Structures:
elements = {  #
    'row 1': {'col 1': 1, 'col 2': True, 'col 3': 'C'},  #
    'row 2': {'col 1': 2, 'col 2': False, 'col 3': 'F'}  #
}

row_2 = elements['row 2']  # get the row 2 dictionary
row_1_col_2 = elements['row 1']['col 2']  # get row 1's col 2

# can also add a new key to the dictionary.
row_3 = {'col 1': 13, 'col 2': 'blue', 'col 3': 'D'}  # create a new row 3 dictionary
elements['row 3'] = row_3  # assign 'row 3' as a key to the elements dictionary