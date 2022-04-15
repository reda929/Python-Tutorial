# Pointers:
# Python does not have C-type memory address, but have a similar, yet changeable, memory address obtained by id()
# at garbage collection time, Python releases a memory address and frees the id(obj) value of that deleted object to be used by other variables,
# meaning id(obj) at one time might change at another
# addressof() is best method to get variable's memory address

# in Python, everything is an object
print (isinstance (1, object))  # True
print (isinstance (list (), object))  # True
print (isinstance (True, object))  # True


def foo ():
    pass


print (isinstance (foo, object))  # True

# every object contains at least three pieces of data:
# 1- Reference count
# 2- Type
# 3- Value

# Immutable vs Mutable Objects:
# Type	    Immutable?
# int	    Yes
# float	    Yes
# bool	    Yes
# complex	Yes
# tuple	    Yes
# frozenset	Yes
# str	    Yes
# list	    No
# set	    No
# dict      No

# id() returns the object’s memory address.
# is returns True if and only if two objects have the same memory address.

# when Python interpreter reads:
# print(300)
# it does the following:
# 1- create an integer object
# 2- give it the value 300
# 3- send it to print() to be printed to the console

print ('merged assignments: ')  # merged assignments:
n = 300
# it creates an integer object, assigns the value 300 to, and points to that object with a reference n
m = n
# can be sure with printing addresses:
# it does not create another object, but simply creates a new reference, m, pointing to the same object that n points to
# for purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256], and strings containing ASCII letters, digits, or underscores only at startup (caches them), and then reuses them during program execution, and just point separate variables references to an integer value in this range, saving memory space. Python caches other datatypes as well like strings less than 20 characters that contain only ASCII letters, digits, and underscores will be interned, as they're assumed to be some kind of identity
# can be sure with printing addresses:
print ('n: ', n, id (n))  # n:  300 2960964114352
print ('m: ', m, id (m))  # m:  300 2960964114352
print (id (n) == id (m))  # True
print ('separate assignments and values: ')  # separate assignments and values:

# but with different values, different addresses are needed
n = 100
m = 200
# now Python creates another int object with the value 100, and points n to it, similarly with m
# now, 300 becomes an orphaned object, i.e., there is no way to access it as no reference points to that integer object 300
# we can see the addresses changed and are no longer identical.
print ('n: ', n, id (n))  # n:  100 2960963079504
print ('m: ', m, id (m))  # m:  200 2960963082704
print (id (n) == id (m))  # False


# modifying a mutable reference creates a new object
x = 5
old_id = id (x)
print ('x: ', x, old_id)
x += 1
new_id = id (x)
print ('x: ', x, new_id)
# notice the different memory addresses
print ('x address matching: ', old_id == new_id)

s = 'abc'
old_id = id (s)
print ('s: ', s, id (s))
s += 'edf'
new_id = id (s)
print ('s: ', s, id (s))
# notice the different memory addresses
print ('s address matching: ', old_id == new_id)

# directly mutating immutable objects (like strings) results in an error:
# s[0] = "R"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# but mutating mutable objects is possible, which does not create a new object
my_list = [1, 2, 3]
old_id = id (my_list)
print ('my_list: ', my_list, id (my_list))  # my_list:  [1, 2, 3] 2081387268672
my_list.append (4)
new_id = id (my_list)
print ('my_list: ', my_list, id (my_list))  # my_list:  [1, 2, 3, 4] 2081387268672
# notice the exact memory addresses
print ('my_list address matching: ', old_id == new_id)  # my_list address matching:  True

my_list[0] = 0
print (my_list)  # [0, 2, 3, 4]
print (id (my_list))  # 140637819575368

# Understanding Variables
# Python's variables are different than variables in C or C++. Python doesn’t even have variables, which are almost the same as variables, except for the pointers' aspect
# to demonstrate how variables work in C, the code
# int x = 2337;
# the following steps are executed:
# 1- allocate enough memory for an integer
# 2- assign the value 2337 to that memory location
# 3- create a pointer, x, to point to that memory address

# then, x would have a memory address of (say 0x7f1, changing at every execution), and value of 2337
# then, if the next code is executed:
# x = 2338;
# then, x would have the same memory address 0x7f1, and OVERWRITE the previous value to be 2338

# x is the memory location, not just a name for it
# int y = x;
# then, y would have a new memory address (say 0x7f5), and a value of 2338, i.e., a new object was created
# therefore, you could modify the value of y without affecting x:
# y = 2339
# then, y would have the same memory address 0x7f5, and a value of 2338
# the value at y has been modified, but not its location
# similarly, the original x was not affected
# this behavior is different from how Python names work.

# for purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256], and strings containing ASCII letters, digits, or underscores only at startup (caches them, or formally, creates an intern object from them), and then reuses them during program execution, and just point separate variables references to an integer value in this range, saving memory space. Python caches other datatypes as well
# strings less than 20 characters that contain only ASCII letters, digits, and underscores will be interned, as they're assumed to be some kind of identity

s1 = "realpython"
print (id (s1))  # 140696485006960
s2 = "realpython"
print (id (s2))  # 140696485006960
print (s1 is s2)  # True
# if we were to introduce other than a non-ASCII letter, digit, or underscore, like panctuation marks for example, a different result would be found:
s1 = "Real Python!"
s2 = "Real Python!"
print (s1 is s2)  # False


# Simulating Pointers in Python (pass by reference):

# 1- using mutable types
#       using lists
def add_one (x):
    x[0] += 1


y = [2337]
add_one (y)
print (y[0])  # 2338

#       using dictionaries
counters = {"func_calls": 0}


def bar ():
    counters["func_calls"] += 1


def foo ():
    counters["func_calls"] += 1
    bar ()


foo ()
print (counters["func_calls"])  # 2


# 2- using objects
class Info:

    def __init__ (self, x, y):
        self.x = x
        self.y = y


    def get_x (self):
        return self.x


    def inc_x (self):
        self.x += 1


    # can possibly override __add__() operators

    def get_y (self):
        return self.y


    def inc_y (self):
        self.y += 1


    def __str__ (self):
        return f'x: {self.x}, y: {self.y}'


myInfo = Info (3, 10)
print ('myInfo: ', myInfo)  # myInfo:  x: 3, y: 10
print ('get_x() before: ', myInfo.get_x ())  # get_x() before:  3
myInfo.inc_x ()
print ('get_x() after: ', myInfo.get_x ())  # get_x() after:  4

print ('get_y() before: ', myInfo.get_y ())  # get_y() before:  10
myInfo.inc_y ()
print ('get_y() after: ', myInfo.get_y ())  # get_y() after:  11

print ('myInfo: ', myInfo)  # myInfo:  x: 4, y: 11

# remember these simulated operations are more expensive than the real pointers in C

from ctypes import addressof, c_int
x = 4
print (hex (id (x)))
print (hex (addressof (c_int (x))))

# two objects with non-overlapping lifetimes may have the same id() value if in .py, not shell prompt

# 3- using ctype
# real pointers in C can be communicated in ctypes functions

# an object’s life begins (integer 300 in this case) when it is created, and stays alive as long as at least one reference points to it, and additional references referring to it may be created and deleted
# when no reference points to that value, Python will eventually notice it is inaccessible, and clear that memory address in that computer to be used later (garbage collection), alongside that id(obj) value

# PEP 8 Naming Conventions suggests:
# snake_case is used for functions and variable names
# PascalCase is used for class names