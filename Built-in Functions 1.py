###########
# BOOLEAN #
###########

# all(iterable): return
# all(iterable): returns True if all elements of iterable are true (or if the iterable is empty), False otherwise
print(all([True, True, True]))  # True
print (all ([True, False, True]))  # False

# any(iterable): returns True if any of the elements of iterable are true (False if the iterable is empty), False otherwise
print (any ([True, True, True]))  # True
print (any ([True, False, False]))  # True
print (any ([False, False, False]))  # False

###########
# NUMBERS #
###########

# sum(iterable, /, start=0): sums start and the items of an iterable from left to right and returns the total
print(sum([2, 5, 6]))  # 13
print(sum([2.2, 5., 6.9]))  # 14.100000000000001
print(sum([2, 5, 6], start = 10))  # 23
print(sum([x for x in range(5, 10)]))  # 35
# For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().

# int(x, base=10): returns an integer x constructed from a number or string x, truncated if x was float
# If x is not a number or if base is given, then x must be a string, bytes, or bytearray representing an integer literal in radix base
# optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace
print(int(21))  # 21
print(int(21.1))  # 21
print(int(21.9))  # 21
print(int('21', base = 3))  # 7
print(int('-21', base = 3))  # -7
print(int('+21', base = 3))  # 7

# bin(x): convert a string of the binary representation of integer x prefixed with “0b”
print(bin(3))  # '0b11'
print(bin(-10))  # '-0b1010'
print(f'{14:#b}', f'{14:b}')  # 0b1110 1110

# oct(x): converts an integer x to an octal string representing it in base 8, prefixed with '0o'
print(oct(8))  #  '0o10'
print(oct(-56))  #  '-0o70'
# can omit the prefix “0o” by either one of the following:
print('%#o' % 10, '%o' % 10)  #  ('0o12', '12')
print(format(10, '#o'), format(10, 'o'))  #  ('0o12', '12')
print(f'{10:#o}', f'{10:o}')  # ('0o12', '12')

# hex(x): converts an integer x to a hexadecimal string prefixed with “0x”
print(hex(255))  # '0xff'
print(hex(-42))  # '-0x2a'
print('%#x' % 255, '%x' % 255, '%X' % 255)  # ('0xff', 'ff', 'FF')
print(format(255, '#x'), format(255, 'x'), format(255, 'X'))  # ('0xff', 'ff', 'FF')
print(f'{255:#x}', f'{255:x}', f'{255:X}')  # ('0xff', 'ff', 'FF')
# input([message]): reads a line from input, converts it to a string (stripping a trailing newline)
# if message is not omitted, input() prompts the user with that message
s = input()
print(s)
s = input('enter: ')
print(s)

# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key]): returns the largest item in an iterable or the largest of two or more arguments. alphabetical sorting is applied. max function is undefined for lists with mixed different, incomparable types
# if multiple items are maximal, the first one encountered is returned
a = ['a', 'b', 'c', 'd']
b = ['e', 'f', 'g']
print(max(a, b))  # ['e', 'f', 'g'], i.e., value is b

# min(iterable, *[, key, default])
# min(arg1, arg2, *args[, key]): returns the smallest item in an iterable or the largest of two or more arguments. alphabetical sorting is applied. min function is undefined for lists with mixed different, incomparable types
# if multiple items are minimal, the first one encountered is returned
a = ['a', 'b', 'c', 'd']
b = ['e', 'f', 'g']
print(min(a, b))  # ['a', 'b', 'c', 'd'], i.e., value is a

# round(number[, ndigits]): returns the number rounded to ndigits precision after the decimal point, and rounds to nearest integer if ndigits is omitted
# for built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits;
# if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2)
# ndigits is any integer value (positive, zero, or negative)
# if ndigits is omitted or None, return value is an integer. otherwise, return value has the same type as number

# WARNING: pay careful attention to rounding is based on 5 (0.5 for ndigits = 0, 0.05, 0.15 .. , 0.95. for ndigits = 1), especially for last example. it's somewhat inconsistent

outset = 0.5
for i in range(2):
    print(f'i = {i}')
    for j in range(5):
        print(f'\t exact: {j + outset:>20}, rounded: {round(j + outset, i):>{i + 4}}')
    for j in range(5):
        print(f'\t exact: {-(j + outset):>20}, rounded: {round(-(j + outset), i):>{i + 4}}')

outset = 2 / 3
for i in range(4):
    print(f'i = {i}')
    for j in range(5):
        print(f'\t exact: {j + outset:>20}, rounded: {round(j + outset, i):>{i + 4}}')
    for j in range(5):
        print(f'\t exact: {-(j + outset):>20}, rounded: {round(-(j + outset), i):>{i + 4}}')

outset = 0.05
for i in range(2):
    print(f'i = {i}')
    for value in ([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05]):
        print(f'\t exact: {value :>20}, rounded: {round(value, i):>{i + 4}}')

###########
# STRINGS #
###########

# class str(object=b'', encoding='utf-8', errors='strict'): returns an str version of object
string = str(3)
print(string, type(string), sep = ', ')  # 3, <class 'str'>
string = str(3.4)
print(string, type(string), sep = ', ')  # 3.4, <class 'str'>
string = str([3, 4])
print(string, type(string), sep = ', ')  # [3, 4], <class 'str'>

# ascii(object): returns a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u, or \U escapes
print(ascii('a أ'))

# chr(i): returns the string of the character from the Unicode code point i
print(chr(97))  # 'a'

# ord(c): returns the Unicode code point of the character c
print(ord('a'))  # 97

# format(value[, format_spec]): converts a value to a “formatted” representation according to format_spec
print('{} {} {}'.format('foo', 'bar', 'baz'))  # 'foo bar baz'

# refer to String Format file for extensive tutorial

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False): prints objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present
# sep and end must be strings
# if no objects are given, print() will just write end (new line by default)
# the file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used
# since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. for such, use file.write(...) instead
# whether the output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
print('foo 42 bar')  # foo 42 bar
print('foo', 42, 'bar')  # foo 42 bar
print('foo', 42, 'bar', sep = '-')  # foo-42-bar
print('foo', end = '/')
print(42, end = '/')
print('bar')  # foo/42/bar
list = [100.768945, 17.232999, 60.98867, 300.837487]
print(['{:.2f}'.format(elem) for elem in list])  # ['100.77', '17.23', '60.99', '300.84']

# refer to Basic Print() file for extensive tutorial

###########
# CLASSES #
###########

# isinstance(object, classinfo): returns True if the object is an instance of the classinfo, or of a (direct, indirect, or virtual) subclass thereof, False otherwise
# if classinfo is a tuple of type objects (or recursively, other such tuples) or a Union Type of multiple types, isinstance() returns True if object is an instance of any of the types

class Parent:
    pass


class Child(Parent):
    pass


p = Parent()
c = Child()
print(type(p))  # <class '__main__.Parent'>
print(type(c))  # <class '__main__.Child'>
print(isinstance(p, Parent))  # True
print(isinstance(p, Child))  # False
print(isinstance(c, Parent))  # True
print(isinstance(c, Child))  # True

# issubclass(class, classinfo): returns True if class is a subclass (direct, indirect, or virtual) of classinfo (a class is considered a subclass of itself), False otherwise
# if classinfo is a tuple of class objects or a Union Type, issubclass() returns if class is a subclass of any entry in classinfo

print(issubclass(Parent, Parent))  # True
print(issubclass(Parent, Child))  # False
print(issubclass(Child, Parent))  # True
print(issubclass(Child, Child))  # True


# class type(object)
# class type(name, bases, dict, **kwds):
# With one argument, returns the type of an object (usually the same object by object.__class__)
# The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.
# With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the __name__ attribute. The bases tuple contains the base classes and becomes the __bases__ attribute; if empty, object, the ultimate base of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the __dict__ attribute. The following two statements create identical type objects:

# TODO Read about and complete type()

class X:
    a = 1


X = type('X', (), dict(a = 1))
print(type('X'))
print(type('X', (), dict(a = 1)))

###################
# DATA STRUCTURES #
###################

# list([iterable]): builds a new list whose items are the same and in the same order as iterable’s items
print(list('abc'))  # ['a', 'b', 'c']
print(list((1, 2, 3)))  # [1, 2, 3]
print(list())  # [] # i.e., a new empty list

# class tuple([iterable]): returns a new tuple object, optionally with elements taken from iterable
print(tuple([3, 5, 2, 3, 6]))  # (3, 5, 2, 3, 6)

# class set([iterable]): returns a new set object, optionally with elements taken from iterable
print(set([3, 5, 2, 3, 6]))  # {2, 3, 5, 6}

# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg): creates a new dictionary from elements of iterable
print(dict((('one', 3), ('two', 5), ('three', 2), ('four', 3), ('five', 6))))  # {'one': 3, 'two': 5, 'three': 2, 'four': 3, 'five': 6}

# map(function, iterable, ...): returns an iterator that applies function to every item of iterable(iterables sequentially), yielding the results
# TODO TUTORIAL

# len(s): returns the length (the number of items) of an object s. argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)
print(len(('12345')))  # 5
print(len(([3, 5, 1])))  # 3

# enumerate(iterable, start=0): returns an enumerate object of an iterable that supports iteration (returns __next__() method of the iterator) a tuple containing a count (from start which defaults to 0) and the values in the iterable: like (0, element1)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start = 1)))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# zip(*iterables, strict=False): iterates over several iterables in parallel, producing tuples with an item from each one
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
# (1, 'sugar')
# (2, 'spice')
# (3, 'everything nice')
# More formally: zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

# zip() is lazy: The elements won’t be processed until the iterable is iterated on
# if iterables have different lengths, zip() stops when the shortest iterable is exhausted, and ignore the remaining items in the longer iterables, cutting off the result to the length of the shortest iterable:
list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))  # [(0, 'fee'), (1, 'fi'), (2, 'fo')]
# to ensure iterables are of the same length, pass strict as True, which will raise an error if lengths are different:
list(zip(('a', 'b', 'c'), (1, 2, 3), strict = True))  # [('a', 1), ('b', 2), ('c', 3)]
# otherwise, any bug resulting from the fact that iterables' lengths are different will be silenced
# zip() in conjunction with the * operator can be used to unzip a list:
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]
print(zip(x, y))
print(*zip(x, y))
print(zip(*zip(x, y)))
x2, y2 = zip(*zip(x, y))
print(x == list(x2) and y == list(y2))  # True

# iter(object[, sentinel])
# Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iterable protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.
# One useful application of the second form of iter() is to build a block-reader. For example, reading fixed-width blocks from a binary database file until the end of file is reached:
# from functools import partial
# with open('mydata.db', 'rb') as f:
#     for block in iter(partial(f.read, 64), b''):
#         process_block(block)

# TODO Read about and complete iter()

# next(iterator[, default]): retrieves the next item from the iterator by calling its __next__() method
# if default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
iter = iter([2, 4, 1])
print(next(iter))  #  2
print(next(iter))  #  4
print(next(iter))  # 1

# sorted(iterable, /, *, key=None, reverse=False): returns a new sorted list from the items in iterable
# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged
nums = [2, 5, 6, 4, 2, 4]
print('nums original before', nums)
print('nums sorted', sorted(nums))
print('nums sorted in reverse', sorted(nums, reverse = True))
print('nums original after', nums)

# sorted() sorts are guaranteed to be stable, i.e., when multiple records have the same key, their original order is preserved
nums_list = [[2, 5], [3, 4], [1, 6], [2, 2], [3, 1]]
print('nums_list sorted', sorted(nums_list))  # nums_list sorted [[1, 6], [2, 2], [2, 5], [3, 1], [3, 4]]  # first: [1, 6],
# second: [2, 5], [2, 2]
# third: [3, 4], [3, 1],
# then,
# first: [1, 6],
# second: [2, 2], [2, 5]
# third: [3, 1], [3, 4],
# then merge. notice, 6 and 5 for first and second lists are not compared (another layer of comparison)
# [[1, 6], [2, 2], [2, 5], [3, 1], [3, 4]]

#################
# MISCELLANEOUS #
#################

# eval(expression[, globals[, locals]]): runs the string representing a valid Python expression and optional globals (dictionary) and locals (a mapping object and could be dictionaries)

# refer to Eval() file for extensive tutorial

# globals(): returns the dictionary implementing the current module namespace
print(globals())

# locals(): updates and returns a dictionary representing the current local dictionary
# at the module level, locals() and globals() are the same dictionary
print(locals())

# vars([object]): returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
# Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).
# Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.
# TODO Read about and complete vars()
print(vars())  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000198AFBB0310>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Coding\\Python\\Tutorial\\Generic Python\\empty3 - Copy (2).py', '__cached__': None}
print(vars() == locals())  # True
