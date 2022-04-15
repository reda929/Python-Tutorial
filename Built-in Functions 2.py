import random


# picking random element from a list
print(random.choice(['apple', 'pear', 'banana']))  # <random element from the list>

# picking n number of random element from range()
print(random.sample(range(100), 10))  # [<random 10 samples between 0 and range(100)>]

# generate random float
print(random.random())  # <random float>

# generate random integer from range()
print(random.randrange(6))  # 4

"""
###################
###################
"""

import statistics


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))  # 1.6071428571428572
print(statistics.median(data))  # 1.25
print(statistics.variance(data))  # 1.3720238095238095

"""
###################
###################
"""

# accessing Internet page
from urllib.request import urlopen


with urlopen('https://docs.python.org') as response:
    for line in response:
        print(f'[{line.decode()}]')

"""
###################
###################
"""

# date formatting
from datetime import date


now = date.today()
print(now)  # datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))  # '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# date uses
birthday = date(1964, 7, 31)
age = now - birthday
y = age.days / 365
m = y % 1 * 12
d = m % 1 * 30
h = d % 1 * 24
M = h % 1 * 60
s = M % 1 * 60
print('age in days: ', age.days)
print('age in seconds: ', age.seconds)
print(f'{int(y)} years, '
      f'{int(m)} months, '
      f'{int(d)} days, '
      f'{int(h)} hours, '
      f'{int(M)} minutes, '
      f'{int(s)} seconds')

"""
###################
###################
"""

# measuring time and execution performance
from timeit import Timer


print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())  # <some time in seconds>
print(Timer('a,b = b,a', 'a=1; b=2').timeit())  # <some time in seconds>

"""
###################
###################
"""
import pprint


t = [[[['a', 'b'], 'c', ['d', 'e']], [['f', 'g'], 'h']]]

pprint.pprint(t, width = 30)
# [[[['a', 'b'],
#    'c',
#    ['d', 'e']],
#   [['f', 'g'],
#    'h']]]
"""
###################
###################
"""
import textwrap


doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

for width in range(10, 100, 10):
    print(f'{"":^>{width}}|')
    print(textwrap.fill(doc, width = width))
    print()
"""
###################
###################
"""
# string templating
# templating typical formatting but for with placeholders arguments to be defined later:

from string import Template


t = Template('|$some|')
print(t.substitute(some = 'abc'))  # |abc|
# can send a dictionary instead:
t = Template('|$some|')
dict = {'some': 'abc'}
print(t.substitute(dict))  # |abc|

# if we needed to write something after a placeholder without a space, it can't be like this:
# t = Template('|$something|')
# as Python thinks 'something' is name of variable as a whole. instead, use braces:
t = Template('|${some}thing|')
print(t.substitute(some = 'abc'))  # |abcthing|

# but substitute() raises an error when a placeholder is not supplied, while safe_substitute() leaves the placeholders unchanged if data is missing

t = Template('|${some}thing|')
# print(t.substitute(something_else = 'abc'))  # KeyError: 'some'
print(t.safe_substitute(something_else = 'abc'))  # |${some}thing|

# Template inheritance can allow using a custom delimiter:
import os.path


photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class MyFormatter(Template):
    delimiter = '%'


fmt = 'myname: [%myname], myid: [%myid], myext: [%myext]'
t = MyFormatter(fmt)

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(myname = base, myid = i, myext = ext)
    print(newname)

# this way, the user can have access to the for-loop, edit the content of MyFormatter dynamically, without changing fmt context (which might be protected by developer, say want to savw user data as '[<id>, <username>, <email>]' and don't want individual users to change this format as database relies on this exact format in storing user data
"""
###################
###################
"""
# logging
# logging module sends log messages to a file or to sys.stderr:
import logging


# notice the difference between standard print() statement and this:
logging.debug('debug message')
logging.info('info message')
logging.warning('warning: file %s not found', 'server.conf')
logging.error('error message')
logging.critical('critical error -- shutting down')
# WARNING:root:warning: file server.conf not found
# ERROR:root:error message
# CRITICAL:root:critical error -- shutting down

# info and debug messages are suppressed by default, and the output is sent to standard error
# other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
"""
###################
###################
"""
# other built-in data structures with different performance trade-offs
# array module provides an array() object that is like a list but only stores homogeneous data in more compactly
# can compactly represent an array of basic values: characters, integers, floating point numbers
# they behave like lists, except that the type of objects stored in them is constrained:

# |Type code| C Type              | Python Type       | Minimum size in bytes|
# |   'b'   | signed char         | int               |           1          |
# |   'B'   | unsigned char       | int               |           1          |
# |   'u'   | wchar_t             | Unicode character |           2          | --- (1)
# |   'h'   | signed short        | int               |           2          |
# |   'H'   | unsigned short      | int               |           2          |
# |   'i'   | signed int          | int               |           2          |
# |   'I'   | unsigned int        | int               |           2          |
# |   'l'   | signed long         | int               |           4          |
# |   'L'   | unsigned long       | int               |           4          |
# |   'q'   | signed long long    | int               |           8          |
# |   'Q'   | unsigned long long  | int               |           8          |
# |   'f'   |  float              | float             |           4          |
# |   'd'   | double              | float             |           8          |
# (1) can be 16 or 32 bits depending on the platform
import sys
from array import array


l = [i for i in range(10000)]
a = array('H', l)
print(sum(a))  # 26932
print(a[1:3])  # array('H', [10, 700])
print(f'size of array: {sys.getsizeof(a)}, #elements = {len(a)}')
print(f'size of list: {sys.getsizeof(l)}, #elements = {len(l)}')
"""
###################
###################
"""
# collections module provides a deque() object that is like a list but with faster appends and pops from the left side but slower lookups in the middle
# well suited for implementing queues and breadth first tree searches

from collections import deque


d = deque(["task1", "task2", "task3"])
print('d before: ', d)
d.append("task4")
print('d after: ', d)
print("Handling", d.popleft())  # Handling task1

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)
"""
###################
###################
"""

# Decimal module
# Decimal reproduces mathematics as done by hand and avoids issues that can arise when binary floating point cannot exactly represent decimal quantities
# applications that require exact decimal representation, high control over precision and rounding like financial and scientific applications where the user expects the results to exactly match calculations done by hand
# e.g., calculating a 5% tax on a 70 cent phone charge:

from decimal import *


print('Decimal: 0.70 * 1.05', round(Decimal('0.70') * Decimal('1.05'), 2))  # Decimal('0.74')
print('regular: 0.70 * 1.05', round(.70 * 1.05, 2))  # 0.73
# Decimsl is able to perform proper modulo calculations and equality tests that are unsuitable for float point numbers:

print(Decimal('1.00') % Decimal('.10'))  # Decimal('0.00')
print(1.00 % 0.10)  # 0.09999999999999995
print(sum([Decimal('0.1')] * 10) == Decimal('1.0'))  # True
print(sum([0.1] * 10) == 1.0)  # False

# The decimal module provides arithmetic with as much precision as needed:
getcontext().prec = 36
print(Decimal(1) / Decimal(7))  # Decimal('0.142857142857142857142857142857142857')