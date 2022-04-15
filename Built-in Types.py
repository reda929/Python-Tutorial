##################
# Built-in Types #
##################

# The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions

############
# Booleans #
############

# Truth Value Testing:
# Any object can be evaluated for truth value
# By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero
# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)
# Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated
# Important exception: the Boolean operations or and and always return one of their operands
print(0 or 'abc') # abc
print('abc' and False) # False

############
# Integers #
############

# int.bit_length(): returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros
# More precisely, for integer x, x.bit_length() returns k such that 2**(k-1) <= abs(x) < 2**k
# if x is zero, then x.bit_length() returns 0
n = -37
print(bin(n)) # '-0b100101'
print(n.bit_length()) # 6

# int.bit_count(): returns the number of ones in the binary representation of the absolute value of the integer, known as population count
n = 19
print(bin(n)) # '0b10011'
print(n.bit_count()) # 3
print((-n).bit_count()) # 3

# int.as_integer_ratio(): returns a pair of integers whose ratio is exactly equal to the original integer and with a positive denominator, which for integer is always the integer itself as the numerator and 1 as the denominator
print((5).as_integer_ratio()) # (5, 1)

#########
# Float #
#########

# float.as_integer_ratio(): returns a pair of integers whose ratio is exactly equal to the original float and with a positive denominator
print((5.5).as_integer_ratio())  # (11, 2)

# float.is_integer(): returns True if the float instance is finite with integral value, and False otherwise
print((-2.0).is_integer()) # True
print((3.2).is_integer()) # False

#############
# Iterators #
#############

# iterators are data structures that implement (container.__iter__() and iterator.__next__()); these are used to allow user-defined classes to support iteration
# sequences always support iteration as well

# container.__iter__(): returns an iterator object
# The iterator objects themselves are required to support the following two methods (known as iterator protocol):

# iterator.__iter__(): returns the iterator object itself

# iterator.__next__(): returns the next item from the iterator

#############
# Generator #
#############

# Generator Types
# Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s __iter__() method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the __iter__() and __next__() methods. More information about generators can be found in the documentation for the yield expression.
#
# Sequence Types — list, tuple, range
# There are three basic sequence types: lists, tuples, and range objects. Additional sequence types tailored for processing of binary data and text strings are described in dedicated sections.
#
# Common Sequence Operations
# The operations in the following table are supported by most sequence types, both mutable and immutable. The collections.abc.Sequence ABC is provided to make it easier to correctly implement these operations on custom sequence types.
#
# This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.
#
# The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (repetition) operations have the same priority as the corresponding numeric operations

# Sequences of the same type also support comparisons. In particular, tuples and lists are compared lexicographically by comparing corresponding elements. This means that to compare equal, every element must compare equal and the two sequences must be of the same type and have the same length. (For full details see Comparisons in the language reference.)
#
# Forward and reversed iterators over mutable sequences access values using an index. That index will continue to march forward (or backward) even if the underlying sequence is mutated. The iterator terminates only when an IndexError or a StopIteration is encountered (or when the index drops below zero).
#
# Notes:
#
# While the in and not in operations are used only for simple containment testing in the general case, some specialised sequences (such as str, bytes and bytearray) also use them for subsequence testing:
#

"gg" in "eggs"
# True
# Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note that items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python programmers; consider:
#

lists = [[]] * 3
lists
# [[], [], []]
lists[0].append(3)
lists
# [[3], [3], [3]]
# What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:
#

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
lists
# [[3], [5], [7]]
# Further explanation is available in the FAQ entry How do I create a multidimensional list?.
#
# If i or j is negative, the index is relative to the end of sequence s: len(s) + i or len(s) + j is substituted. But note that -0 is still 0.
#
# The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. If i or j is greater than len(s), use len(s). If i is omitted or None, use 0. If j is omitted or None, use len(s). If i is greater than or equal to j, the slice is empty.
#
# The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached (but never including j). When k is positive, i and j are reduced to len(s) if they are greater. When k is negative, i and j are reduced to len(s) - 1 if they are greater. If i or j are omitted or None, they become “end” values (which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.
#
# Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:
#
# if concatenating str objects, you can build a list and use str.join() at the end or else write to an io.StringIO instance and retrieve its value when complete
#
# if concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO, or you can do in-place concatenation with a bytearray object. bytearray objects are mutable and have an efficient overallocation mechanism
#
# if concatenating tuple objects, extend a list instead
#
# for other types, investigate the relevant class documentation
#
# Some sequence types (such as range) only support item sequences that follow specific patterns, and hence don’t support sequence concatenation or repetition.
#
# index raises ValueError when x is not found in s. Not all implementations support passing the additional arguments i and j. These arguments allow efficient searching of subsections of the sequence. Passing the extra arguments is roughly equivalent to using s[i:j].index(x), only without copying any data and with the returned index being relative to the start of the sequence rather than the start of the slice.

############################
# Immutable Sequence Types #
############################

#
# The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the hash() built-in.
#
# This support allows immutable sequences, such as tuple instances, to be used as dict keys and stored in set and frozenset instances.
#
# Attempting to hash an immutable sequence that contains unhashable values will result in TypeError.
#
# Mutable Sequence Types
# The operations in the following table are defined on mutable sequence types. The collections.abc.MutableSequence ABC is provided to make it easier to correctly implement these operations on custom sequence types.
#
# In the table s is an instance of a mutable sequence type, t is any iterable object and x is an arbitrary object that meets any type and value restrictions imposed by s (for example, bytearray only accepts integers that meet the value restriction 0 <= x <= 255)

############################
# XXX #
############################

# Notes:
#
# t must have the same length as the slice it is replacing.
#
# The optional argument i defaults to -1, so that by default the last item is removed and returned.
#
# remove() raises ValueError when x is not found in s.
#
# The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. To remind users that it operates by side effect, it does not return the reversed sequence.
#
# clear() and copy() are included for consistency with the interfaces of mutable containers that don’t support slicing operations (such as dict and set). copy() is not part of the collections.abc.MutableSequence ABC, but most concrete mutable sequence classes provide it.
#
# New in version 3.3: clear() and copy() methods.
#
# The value n is an integer, or an object implementing __index__(). Zero and negative values of n clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for s * n under Common Sequence Operations.

#########
# Lists #
#########

# Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).
list = [5, 2, 3, 6, 3]
print(list)

# sort(*, key=None, reverse=False): sorts the list in place, using only < comparisons between items
# if any comparison operations fail, the entire sort operation will fail (and the list will likely be left in a partially modified state)
list.sort()
print('list sorted: ', list)
non_homogenous_list = [3, 4, 6, 2, 5, 'a', 1]
try:
    non_homogenous_list.sort()
    print('non_homogenous_list sorted successfully: ', non_homogenous_list)
except:
    print('non_homogenous_list was not sorted successfully: ', non_homogenous_list)
list.sort(reverse = True)
print('list sorted in reverse: ', list)

# key specifies a function of one argument whose return value is used for comparison (default value of None means values are compared directly without preprocessing)

def func(x):
    return (x % 4) * (x % 5)


for i in (list):
    print(f'func({i}): {func(i)}')
list.sort(key = func)
print('list sorted: ', list)

# sorted() sorts are guaranteed to be stable, i.e., when multiple records have the same key, their original order is preserved
nums_list = [[2, 5], [3, 4], [1, 6], [2, 2], [3, 1]]
print('nums_list sorted', sorted(nums_list))  # nums_list sorted [[1, 6], [2, 2], [2, 5], [3, 1], [3, 4]]  # first: [1, 6],  # second: [2, 5], [2, 2]
# third: [3, 4], [3, 1],
# then,
# first: [1, 6],
# second: [2, 2], [2, 5]
# third: [3, 1], [3, 4],
# then merge. notice, 6 and 5 for first and second lists are not compared (another layer of comparison)
# [[1, 6], [2, 2], [2, 5], [3, 1], [3, 4]]

##########
# Ranges #
##########

# class range(stop)
# class range(start, stop[, step]): returns an immutable sequence of numbers arguments, starting at start (defaults to 0), stopping at when value reaches or exceeds stop, incrementing/decrementing step (defaults to 1) each time. start, stop and step must be integers (either built-in int or any object that implements the __index__() special method)

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 5)))  # [0, 5, 10, 15, 20, 25]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(range(0)))  # []
print(list(range(1, 0)))  # []

# range will always only take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values (and not entire sequence of integerss, calculating individual items and subranges as needed)
r = range(0, 20, 2)
print(r)  # range(0, 20, 2)
for i in r:
    print(i)

# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
print(11 in r)  # False
print(10 in r)  # True
print(r.index(10))  # 5
print(r[5])  # 10
print(r[:5])  # range(0, 10, 2)
print(r[-1])  # 18

#############
# Set Types #
#############

# Set Types: set, frozenset
# There are currently two built-in set types, set and frozenset
# contents can be changed using methods like add() and remove()
# frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.
# Non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: {'jack', 'sjoerd'}, in addition to the set constructor.

# class set([iterable])
# class frozenset([iterable]): returns a new set or frozenset object whose elements are from iterable
# to represent sets of sets, the inner sets must be frozenset objects. If iterable is not specified, a new empty set is returned.
# isdisjoint(other): returns True if set has no elements in common with other
# sets are disjoint if and only if their intersection is the empty set
print(({1, 2, 3}).isdisjoint({3, 4, 5}))  # False
print(({1, 2, 3}).isdisjoint({4, 5, 6}))  # True

a, b, c = {1, 2, 3}, {3, 4, 5}, {1, 2, 3, 4, 5, 6, 7, 8, 9}

# set.issubset(other): returns True if set is a subset of or equal to other
# set <= other: returns True if set is a subset of or equal to other
# set < other: returns True if set is a subset of but is not other

# set.issuperset(other): returns True if set is a superset of or equal to other
# set >= other: returns True if set is a superset of or equal to other
# set > other: returns True if set is a superset of or equal but is not other

# set.union(*others): return a new set with elements from set and all others
# set | other | ...: return a new set with elements from set and all others

# set.intersection(*others): return a new set with elements common to set and all others
# set & other & ...: return a new set with elements common to set and all others

# set.difference(*others): return a new set with elements in set that are not in others
# set - other - ...: return a new set with elements in set that are not in others

# set.symmetric_difference(other): return a new set with elements in either set or other but not both

# set.copy(): return a shallow copy of set

# methods (union(), intersection(), difference(), symmetric_difference(), issubset(), and issuperset()) accept any iterable as an argument, while their operator based counterparts require their arguments to be sets, which precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs')

# set.update(*others): updates set, adding elements from all others
# set |= other | ...: updates set, adding elements from all others

# set.intersection_update(*others): updates set, keeping only elements found in set and all others
# set &= other & ...: updates set, keeping only elements found in set and all others

# set.difference_update(*others): updates set, removing elements found in others from set
# set -= other | ...: updates set, removing elements found in others from set

# set.symmetric_difference_update(other): updates set, keeping only elements found in either set, but not in both
# set ^= other: updates set, keeping only elements found in either set, but not in

# set.add(elem): adds element elem to set
# set.remove(elem): removes element elem from set, raises KeyError if elem is not contained in set
# set.discard(elem): removes element elem from set, does not raise KeyError
# set.pop(): removes and returns an arbitrary element from set, raises KeyError if set is empty
# set.clear(): removes all elements from set
# methods (update(), intersection_update(), difference_update(), and symmetric_difference_update()) accept any iterable as an argument
# __contains__(), remove(), and discard() accept set as arguments

#################
# Mapping Types #
#################

# Mapping Types — dict
# mapping object is a mutable object that maps hashable values to arbitrary objects, currently there is only one standard mapping type, the dictionary

###########
# Hashing #
###########

# hashing, loosely speaking, is a multiple-to-one function that returns a unique output value to every unique input value
# function is such that even when knowing the output:
# 1- being able to differentiate that two inputs were different even without knowing they those values were
# 2- hashing a value will never change (either in a program's life time, or at all)
# 3- it's almost impossible to unhash (figure out what the input was), either because impossibility (like x^2 can know if x was pos or neg for real x), or practical constraints (taking too much space and/or time to calculate calculate)

# immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable
# objects which are instances of user-defined classes are hashable by default. they all are unequal (except with themselves), and their hash value is derived from their id()
# hashing function is a function which takes an object, say a string such as “Python,” and returns a fixed-size value, say an integer
# different versions of Python are free to change the underlying hash function, but no matter now many times I run hash('Python') for the same Python version, I'll always get the same result
print(f"Python hash: {hash('Python')}")
# but hashing a different value will return a different value
print(f"Java hash: {hash('Java')}")
print(f"frozenset hash: {hash(frozenset({1, 2}))}")
print(f"tuple hash: {hash((1, 2))}")

# some objects and operations, like dictionaries, require the keys to be immutable
# hashable, is a mutable type that supports hash(), otherwise call will fail
# print(f"list hash: {hash([1, 2])}") # TypeError: unhashable type: 'list'
# even though sets are immutable, they are not always hashable:
# print(f"set hash: {hash({1, 2})}") # TypeError: unhashable type: 'set'
# print(f"dict hash: {hash({1: 2})}") # TypeError: unhashable type: 'dict'

# some purposes for hashing objects are to:
# Convert variable-length keys into fixed length values, by folding them by words or other units
# Scramble the bits of the key so that the resulting values are uniformly distributed over the keyspace
# Map the key values into ones less than or equal to the size of the table

# a good hash function satisfies two basic properties:
# 1- very fast to compute
# 2- should minimize duplication of output values (collisions)
# hash functions rely on generating favourable probability distributions for their effectiveness, reducing access time to nearly constant (which could reveal some info about the underlying algorithm)

# a dictionary’s keys are almost arbitrary, but hashable values:
# keys of numeric types that obey the normal rules for numeric comparison: being equal even for different data types (such as 1 and 1.0) can be used interchangeably to index the same dictionary entry (but since computers store floating-point numbers as approximations, it is usually unwise to use them as dictionary keys)
# an object is hashable if it has a hash value which never changes during its lifetime:
# needs a __hash__() method),
# can be compared to other objects (has an __eq__() method), and
# equal hashable objects must have the same hash value

# class dict(**kwargs)
# class dict(mapping, **kwargs)
# class dict(iterable, **kwargs): returns a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments
# if a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary
# If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument
# if a key being added is already present, keyword argument overrides the value from the positional argument

# all the following examples return a dictionary equal to {"one": 1, "two": 2, "three": 3}:
a = dict(one = 1, two = 2, three = 3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two = 2)
dicts = [a, b, c, d, e, f]
for i, d in enumerate(dicts):
    print(f"{chr(ord('a') + i)}: {d}")

# notice though  d, e and f differ from the rest in order, their keys and values match other dictionaries
# a: {'one': 1, 'two': 2, 'three': 3}
# b: {'one': 1, 'two': 2, 'three': 3}
# c: {'one': 1, 'two': 2, 'three': 3}
# d: {'two': 2, 'one': 1, 'three': 3}
# e: {'three': 3, 'one': 1, 'two': 2}
# f: {'one': 1, 'three': 3, 'two': 2}
print(a == b == c == d == e == f)  # True

# note that as long as keyword arguments are valid Python identifiers, they can be used as keys
dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

# dictionaries operations support (and custom mapping types should also support):
# list(d): returns a list of all the keys used in dictionary d
print(f'list(dict): {list(dict)}')  # list(dict): ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# len(d): returns the number of items in the dictionary d
print(f'len(dict): {len(dict)}')  # len(dict): 10

# d[key]: returns the item of d with key key. Raises a KeyError if key is not in the map
print(f"dict['two']: {dict['two']}")  # dict['two']: 2

# if a subclass of dict defines a method __missing__() and key is not present, the d[key] operation calls that method with the key key as argument, and the d[key] operation returns or raises whatever is returned or raised by the __missing__(key) call
# no other operations or methods invoke __missing__()
# if __missing__() is not defined, KeyError is raised. __missing__() must be a method

# class DictSubclass(dict):
#
#     def __missing__(self, key):
#         return 0
#     def __getitem__(self, item):
#         return 0
#     def __delitem__(self, item):
#         return None
#
# c = DictSubclass()
# print(c)
# print(c['red'])
# c['red'] += 1
# print(c['red'])
#
# # d[key] = value: sets d[key] to value
# c['red'] = 5
# print(c)
#
# # del map[key]: removes map[key] from dictionary map. Raises a KeyError if key is not in the map
# del c['red']
# print(c)

# key in dict: returns True if dict has a key key, else False
print(f"'one' in dict: {'three' in dict}")  # 'one' in dict: True
print(f"'twelve' in dict: {'twelve' in dict}")  # 'twelve' in dict: False

# key not in dict: equivalent to not key in dict
print(f"'three' not in dict: {'three' not in dict}")  # 'three' not in dict: False
print(f"'twelve' not in dict: {'twelve' not in dict}")  # 'twelve' not in dict: True

# iter(dict): returns an iterator over the keys of the dictionary (shortcut for iter(dict.keys())
for k, v in enumerate(iter(dict)):
    print(f"k = {k}: {v}")
# k = 0: one
# k = 1: two
# k = 2: three
# k = 3: four
# k = 4: five
# k = 5: six
# k = 6: seven
# k = 7: eight
# k = 8: nine
# k = 9: ten

# dict.copy(): returns a shallow copy of the dictionary
dict_copy = dict.copy()
print(f'dict.copy(): {dict_copy}')  # dict.copy(): {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
print(f'id(dict): {id(dict)}\n'
      f'id(dict_copy): {id(dict_copy)}\n'
      f'id(dict) == id(dict_copy): {id(dict) == id(dict_copy)}')
# id(dict): 2062638202944
# id(dict_copy): 2062638203008
# id(dict) == id(dict_copy): False

# dict.clear(): removes all items from the dictionary
dict_copy.clear()
print(f'dict_copy.clear() : {dict_copy}')  # dict_copy.clear() : {}

# classmethod fromkeys(iterable[, value]): TODO method

# dict.get(key[, default]): returns the value for key if key is in the dictionary, else default, or if default is not given then returns None
print(f"'two' in dict: {'two' in dict}, dict.get('two'): {dict.get('two')}")  # 'two' in dict: True, dict.get('two'): 2
print(f"'twelve' in dict: {'twelve' in dict}, dict.get('twelve', 5): {dict.get('twelve', 5)}")  # 'twelve' in dict: False, dict.get('twelve', 5): 5

# dict.items(): returns a new view of the dictionary’s items ((key, value) pairs)
print(f'dict.items(): {dict.items()}')  # dict.items(): dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10)])

# dict.keys(): returns a new view of the dictionary’s keys
print(f'dict.keys(): {dict.keys()}')  # dict.keys(): dict_keys(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])

# dict.values(): returns a new view of the dict’s values
print(f'dict.values(): {dict.values()}')  # dict.values(): dict_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# dict.pop(key[, default]): if key is in the dictionary, removes it and returns its value, else returns default, or if default is not given and key is not in the dict then returns None
print(f"dict.pop('three'): {dict.pop('three')}")  # dict.pop('three'): 3
print(f"dict: {dict}")  # dict: {'one': 1, 'two': 2, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
print(f"dict.pop('three', 100): {dict.pop('three', 100)}")  # dict.pop('three', 100): 100
print(f"dict: {dict}")  # dict: {'one': 1, 'two': 2, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

# dict.popitem(): removes and returns a (key, value) pair from the dictionary in the same order elements were added, i.e., LIFO (last in, first out)
# dict.popitem() is useful to destructively iterate over a dictionary
print(f'dict.popitem(): {dict.popitem()}')  # dict.popitem(): (<random dict pair>)

# reversed(dict): returns a reverse iterator over the keys of the dictionary (shortcut for reversed(d.keys()))

print('reversed(dict):')
for k, v in enumerate(reversed(dict)):
    print(f'{k}: {v}')
# 0: nine
# 1: eight
# 2: seven
# 3: six
# 4: five
# 5: four
# 6: two
# 7: one

# dict.setdefault(key[, default]): if key is in the dictionary, returns its value
# if not, insert key with a value of default and returns default (default defaults to None)
print(f"dict.setdefault('one'): {dict.setdefault('one')}")  # dict.setdefault('one'): 1
print(f"dict.setdefault('three', 100): {dict.setdefault('three', 100)}")  # dict.setdefault('three', 100): 100

# dict.update([other]): updates the dictionary with the key/value pairs from other, overwriting existing keys (d.update(k1 = v1, k2 = v2))
# dict.update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two)
print(f"dict.update([['one', 111], ['two', 222]]): {dict.update([['one', 111], ['two', 222]])}")  # dict.update([['one', 111], ['two', 222]]): None
# dict | other: creates a new dictionary with the merged keys and values of dictionary dict and dictionary other, with other overriding any common keys

# dict |= other: updates dictionary dict with keys and values of other (may be either a mapping or an iterable of key/value pairs), with other overriding any common keys

# dictionaries preserve insertion order (even keys added after being deleted are inserted at the end), with updating a key not affecting the order
keys = dict.keys()
values = dict.values()

print(f"dict.keys(): {dict.keys()}")  # dict.keys(): dict_keys(['one', 'two', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'three'])
print(f"dict.values(): {dict.values()}")  # dict.values(): dict_values([111, 222, 4, 5, 6, 7, 8, 9, 100])
# set operations
print(f"keys & {'one', 'twenty', 'three'}: {keys & {'one', 'twenty', 'three'} }")  # keys & ('one', 'twenty', 'three'): {'one', 'three'}
print(f"keys ^ {'fifteen', 'six'}: {keys ^ {'fifteen', 'six'} }")  # keys ^ ('fifteen', 'six'): {'fifteen', 'four', 'five', 'seven', 'three', 'eight', 'one', 'nine', 'two'}
# get back a read-only proxy for the original dictionary
print(f"values.mapping: {values.mapping}")  # values.mapping: {'one': 111, 'two': 222, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'three': 100}
print(f"values.mapping['spam']: {values.mapping['five']}")  # values.mapping['spam']: 5


##############
# Union Type #
##############

# Union Type
# print(f'XXX: {}')
# a union object holds the value of the | (bitwise or) operation on multiple type objects for objects' comparison
# X | Y | ...:
# defines a union object which holds types X, Y (X | Y means either X or Y)

# the following function expects an argument of type int or float:

def square(number: int | float) -> int | float:
    return number ** 2


print(square(4))  # 16
print(square(1.5))  # 2.25
exit()
# union_object == other
# Union objects can be tested for equality with other union objects. Details:

# unions' attributes:
# (int | str) | float
# is equivalent to:
# int | str | float

# Redundant types are removed:
# int | str | int
# is equivalent to:
# int | str

# When comparing unions, the order is ignored:
# int | str
# is equivalent to:
# str | int

# int | str
# is equivalent to:
# typing.Union[int, str]

# str | None
# is equivalent to:
# typing.Optional[str]

# Calls to isinstance() and issubclass() are also supported with a union object:
# isinstance(obj, union_object)
# issubclass(obj, union_object)
print(isinstance("", int | str))  # True

# However, union objects containing parameterized generics cannot be used:
# print(isinstance(1, int | list[int])) # TypeError: isinstance() argument 2 cannot contain a parameterized generic

# The user-exposed type for the union object can be accessed from types.UnionType and used for isinstance() checks. An object cannot be instantiated from the type:

import types


print(isinstance(int | str, types.UnionType))  # True
print(types.UnionType())  # TypeError: cannot create 'types.UnionType' instances


# Note The __or__() method for type objects was added to support the syntax X | Y. If a metaclass implements __or__(), the Union may override it:

class M(type):

    def __or__(self, other):
        return "Hello"


class C(metaclass = M):
    pass


print(C | int)  # 'Hello'
print(int | C)  # int | __main__.C


# Methods
class C:

    def method(self):
        pass


c = C()
# can't set on the method
# c.method.whoami = 'my name is method' # AttributeError: 'method' object has no attribute 'whoami'
c.method.__func__.whoami = 'my name is method'
print(c.method.whoami)  # 'my name is method'