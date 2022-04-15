# *args and **kwargs meaning in my_function(arg1, arg2, arg3, *args, **kwargs)
# a single asterisk (*) unpack iterables (like positional argument)
# two asterisks (**) unpack dictionaries ('end': '-', 'sep': ',')

# the iterable object of unpacking operator * (*integers) is a tuple
def print_args (*integers): # here, args is integers, i.e., *args is *integers
    print('arguments: [', end='')
    for x in integers:
        print(x, ', ', end = '', sep = '')
    print(']')

print_args (1, 2, 3)

# unpacking operator (**)

# printing values
def print_dict_vals (**words):  # here, kwargs is words, i.e., **kwargs is **words
    print ('dictionary values: [', end = '')
    for x in words.values ():
        print (x, ', ', end = '', sep = '')
    print (']')


print_dict_vals (a = "Real", b = "Python", c = "Is", d = "Great", e = "!")

# printing keys
def print_dict_keys (**words):
    print ('dictionary keys: [', end = '')
    for x in words:
        print (x, ', ', end = '', sep = '')
    print (']')


print_dict_keys (a = "Real", b = "Python", c = "Is", d = "Great", e = "!")

# creating a function with changeable number of both positional and named arguments
# just like non-default arguments have to precede default arguments in normal functions, the following order must hold:
# 1- standard arguments
# 2- *args arguments
# 3- **kwargs arguments

# this function definition is correct:
# def my_function(a, b, *args, **kwargs):
#     pass

# but this function definition is incorrect, and will throw a SyntaxError:
# def my_function(a, b, **kwargs, *args):
#     pass
# just like writing a normal function is incorrect:
# def my_function(4, 5, name = 'John', '43802'):
#     pass
# because **kwargs  which is {'name' = 'John'} preceded *args which is ['43802']

# printing a list normally:
my_list = [1, 2, 3]
print (my_list)
# unpacking the list first, then printing the content individually:
my_list = [1, 2, 3]
print (*my_list)
# which can be better understood with:
print (*my_list, sep = '-')
# which is the equivalent of print (1, 2, 3, sep = '-')
# which means we can pass multiple lists as print(*list1, *list2, *list3) as unpacking will unpack lists one by one

# strings are also iterables, which means:
a = [*'RealPython']
print (a)  # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

# can split a list into multiple parts
# can unpack first value, all values inbetween first and last value, and the last value
# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print (a)
print (b)
print (c)
# 1
# [2, 3, 4, 5]
# 6

# merging lists
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]
print (my_merged_list)  # [1, 2, 3, 4, 5, 6]

# merging dictionaries
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print (my_merged_dict)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4}