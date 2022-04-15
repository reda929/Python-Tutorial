# Method 1:
# %-formatting
# it may fail to display tuples and dictionaries correctly, and can be lengthy and confusing for longer strings

print ("%s" % 'text')  # 'text'
print ("%s %s" % ('text', 'field'))  # 'text field'

# can use variables as well
name = 'Winston'
age = 24
print (f'Hello, {name}. You are {age}.')  # Hello, Winston. You are 24.
print (f"Hello, {name + ' Smith'}. In 50 years, you'll be {age + 50}.")  # Hello, Winston. In 50 years, you'll be 74.
print ('|%20s|' % ('geeksforgeeks',)) # |       geeksforgeeks|
print ('|%-20s|' % ('Interngeeks',)) # |Interngeeks         |
print ('|%.5s|' % ('Interngeeks',))  # |Inter|

# Method 2:
# str.format()-formatting
# can use positional argument formatting method or keyword argument formatting method

# instead of:
print ('%d %s cost %.2f dollar' % (6, 'bananas', 1.745))  # '6 bananas cost $1.75 dollar'
# you can use:
# 1) positional argument formatting:
print ('{0} {1} cost {2} dollar'.format (6, 'bananas', 1.745))  # '6 bananas cost 1.745 dollar'
# replacement fields don’t have to appear in numerical order
print ('{2} {0} {1}'.format ('foo', 'bar', 'baz'))  # 'babaz foo bar'

# in Python 3.1, you can omit numbering; sequential order is assumed
print ('{} {} {}'.format ('foo', 'bar', 'baz'))  # 'foo bar baz'

# 2) keyword argument formatting:
print ('{quantity} {item} cost {price} dollar'.format (quantity = 6, item = 'bananas', price = 1.745))  # '6 bananas cost $1.75'
# can use both positional and keyword arguments in format() call
print ('{0}{1}{x}'.format ('foo', 'bar', x = 'baz'))  # 'foobarbaz'
# notice no positional argument is defined before a variable
print ('{0}{x}{1}'.format ('foo', 'bar', x = 'baz'))  # 'foobazbar'

# Detailed Formatting:
# for a string containing replacement_field in it, replaced with 	, i.e.,'|replacement_field| is formatted'.format (format_spec)

# str.format() Method: Simple Replacement Fields
# {[<name>][!<conversion>][:<format_spec>]}
# all fields are optional and may be omitted
# <name>: index of argument, or keyword argument
# <conversion>: data type conversion to apply on the formatted value
# <format_spec>: encapsulates more detail about how the value should be converted

# The <name> Component
# indicates which argument from the argument list is inserted into the given location.
# either a number for a positional argument, or a keyword for a keyword argument
# positional argument
x, y, z = 1, 2, 3
print ('{0}, {1}, {2}'.format (x, y, z))  # '1, 2, 3'
# keyword argument
a = ['foo', 'bar', 'baz']
print ('{0[0]}, {0[2]}'.format (a))  # 'foo, baz'
# 0[2], where 0 is first argument, i.e., a, and 2 is index, giving 'baz'
d = {'key1': 'foo', 'key2': 'bar'}
print ('{0[key1]}'.format (d))  # 'foo'
# 0[key1] same as above, except we're indexing with a string 'key1' instead of integers
# works for class objects as well
class Employee:
    def __init__ (self, name):
        self.name = name
emp1 = Employee ('John')
print ('employee\'s name is {0.name}'.format (emp1))  # 'employee's name is John'

# The <conversion> Component:
# format a string using three different an object's attributes: str() (default), repr() or ascii()
# !s	Convert with str()
# !r	Convert with repr()
# !a	Convert with ascii()
print ('{0!s}'.format (42))  # '42'
print ('{0!r}'.format (42))  # '42'
print ('{0!a}'.format (42))  # '42'
# Python accesses argument's (42 in this case, or any object) __str__ and __repr__ attributes of the object
# In many cases, the result is the same regardless of which conversion function you use

# The general form of a standard format specifier is:
# format_spec:  [[fill]align][sign][#][0][width][grouping_option][.precision][conversion]
# fill: <any character except for braces '{' and '}'> # character to pad rest of field width with
# align: "<" | ">" | "=" | "^"
# sign: "+" | "-" | " "
# #: displays alternate form integers, (prefix respective '0b', '0o', or '0x' for binary, octal, or hexadecimal)
# 0: zero trailing for numeric values.
# width: integer
# grouping_option: "_" | ","
# precision: integer # Specifies the number of digits after the decimal point for floating-point presentation types, and the maximum output width for string presentations types
# conversion        :  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%" # specifies conversion method of argument

n = 12.3456
# fill:
# '=': allows padding for digits
print ('|{:a=8.0f}|'.format (n))  # '|aaaaaa12|' i.e., float number with 0 decimal digits all in 8 field width, filled with 'a' on the rest of field
print ('|{:!<8s}|'.format ('Z'))  # '|Z!!!!!!!|'i.e., 'Z' string in 8 field width, left justified, filled with '!' on the rest of field

# align:
# '<': field will be left-aligned within the available space (default for strings)
# '>': field will be right-aligned within the available space(default for numbers)
# '^': field will be centered within available space
print ('|{:>8s}|'.format ('Z'))  # '|       Z|'
print ('{:^5d}'.format (12))  # ' 12  '
# '=': sign will appears at the left edge of the output field, and padding is placed in between the sign and the number
# even though alignment for numbers is to the right, '=' forces filling between sign and last left digit character
print ('|{0:@>+6d}|'.format (123))  # |@@+123|
print ('|{0:@=+6d}|'.format (123))  # |+@@123|

# sign:
# -: The converted value is left adjusted, adds a minus sign if needed, blank space otherwise
# +: A sign character (+ or -) will precede the output within available space
print ('{:+3d}'.format (12))  # '+12'
print ('{:+3d}'.format (-12))  # '-12'
print ('{:3d}'.format (12))  # ' 12'
print ('{: 3d}'.format (-12))  # '-12'
print ('{:-3d}'.format (12))  # ' 12'
print ('{:-3d}'.format (-12))  # '-12'

# sign is placed directly to the left of the first digit in the number by default, if sign = '=' was not used
print ('|{:+6d}|'.format (123))  # |  +123|
print ('|{:=+6d}|'.format (123))  # |+  123|
print ('|{:+6d}|'.format (-123))  # |  -123|
print ('|{:=+6d}|'.format (-123))  # |-  123|

# #:
print ('{:#x}'.format (47))  # '0x2f'
print ('|{:#05x}|'.format (47))  # '|0x02f|'

# 0:
# '=': allows padding but with signs, as in '+000000120'
# notice sign takes space from field width
print ('{:05d}'.format (12))  # '00012'
print ('{:=+05d}'.format (12))  # '+0012'
print ('{:=+05d}'.format (-12))  # '-0012'

# width:
print ('|{0:10s}|'.format ('Text'))  # '|Text      |'

# grouping_option:
# ',': field will use thousands' comma (every 3 digits) separator
# '_': field will use thousands' comma (every 3 digits) separator, every 4 digits for binary
print ('{:,}'.format (78962324245))  # '78,962,324,245'
print ('{:,d}'.format (78962324245))  # '78,962,324,245'
print ('{:_d}'.format (78962324245))  # '78_962_324_245'
print ('{:,.2f}'.format (5897653423.89676))  # '5,897,653,423.90'
print ('{:_.2f}'.format (5897653423.89676))  # '5_897_653_423.90'

# precision:
print ('|{:.2f}|'.format (n))  # '| 12.35|' i.e., float number with 2 decimal digits
print ('{:.4s}'.format ('foobar')) # 'foob'

# Conversions:
# n     : integer | float with least needed precision
# d     : integer
# b     : binary
# f	| F : float (default precision is 6)
# e | E : float in exponential format/scientific notation (default precision is 6)
# g | G : exponential format if exponent < -4 or > 5 , decimal format otherwise
# o     : octal
# x | X : hexadecimal
# c     : character
# r     : string converted with repr()
# s     : string converted with str()
# '%'   : percentage (number * 100 in 'f' format, followed by a percent sign)
# using lower or upper case only affects letter case in output, but has the same effect otherwise

print ('{:n}'.format (47))  # '47'
print ('{:n}'.format (47.3))  # '47.3'
print ('{:n}'.format (0x2f))  # '47'
print ('{:d}'.format (47))  # '47'
print ('{:b}'.format (47))  # '101111'
print ('{:f}'.format (47))  # '47.000000'
print ('{:f}'.format (47.3))  # '47.300000'
print ('{:e}'.format (356.08977))  # '3.560898e+02'
print ('{:g}'.format (1E+6))  # 1e+06
print ('{:g}'.format (1E+5))  # 100000
print ('{:g}'.format (1E+4))  # 10000
print ('{:g}'.format (1E-4))  # 0.0001
print ('{:g}'.format (1E-5))  # 1e-05
print ('{:o}'.format (47))  # '57'
print ('{:x}'.format (47))  # '2f'
print ('{:#x}'.format (47))  # '0x2f'
print ('|{:#5x}|'.format (47))  # '| 0x2f|'
print ('{:c}'.format (65))  # 'A'
print ('{:s}'.format ('A'))  # 'A'
print ('{:%}'.format (1.3))  # '130.000000%'
print ('{:.3%}'.format (1 / 7))  # '14.286%'

# can override a class'  __format__() method
class Person:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def __str__ (self):
        return 'This is |{}|\'s string'.format (self.name)  # 'format(name): I am John'

    def __repr__ (self):
        return 'This is |{}|\'s representation'.format (self.name)  # 'format(age): I am 29 years old'

    def __format__ (self, format):
        if (format == 'name'):
            return 'format(name): I am {}'.format (self.name)  # 'This is |John|'s string'
        elif (format == 'age'):
            return 'format(age): I am {} years old'.format (self.age)  # 'This is |John|'s representation'

p = Person ('John', 29)
print (format (p, 'name'))
print (format (p, 'age'))
print ('{!s}'.format (p))
print ('{!r}'.format (p))

# some built-in classes have built-in formatting:
import datetime
d = datetime.datetime (2010, 7, 4, 12, 15, 58)
print ('{:Year: %Y\nMonth: %m\nDay: %d\nHour: %H\nMinute: %M\nSecond: %S}'.format (d))  # Year: 2010# Month: 07
# Day: 04
# Hour: 12
# Minute: 15
# Second: 58

# dynamic formatting
print ('{n:{0}.{1}f}'.format (10, 2, n = 123.456))  # '    123.46'

# Method 3:
# for any expression
# '{0!<conversion>:<format_spec>}'.format(<expr>)
# can be expressed with f-string like:
# f'{<expr>!<conversion>:<format_spec>}'

# Basic f-string
s = 'bar'
print (f'{s}')  # bar
print (f'a\n{s}\nb')
# a
# bar
# b

age = 13
print(f"I am {'a minor' if age < 18 else 'an adult'}") # I am a minor
# Using variables
name = 'Eric'
age = 74
print (f'Hello, {name}. You are {age}.')  # 'Hello, Eric. You are 74.'

# Printing lists and dictionaries
a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}
print (f'a = {a} | d = {d}')
# a = ['foo', 'bar', 'baz'] | d = {'foo': 1, 'bar': 2}
print (f'first element: {a[0]}')  # first element: foo
print (f'last two elements: {a[-2:]}')  # last two elements: ['bar', 'baz']
print (f'list reversed: {a[::-1]}')  # list reversed: ['baz', 'bar', 'foo']
print (f"d['bar']: {d['bar']}")  # d['bar']: 'bar' 2

# Using functions:
a = ['foo', 'bar', 'baz', 'qux', 'quux']
print (f'list\'s length: {len (a)}')  # list's length: 5
print (f'{s.upper ()}') # BAR

# Multiline f-Strings
# an 'f' needs to be in front of each line of a multiline string, but is printed with no newlines
name = 'Eric'
profession = 'comedian'
affiliation = 'Monty Python'
message = (f'Hi {name}'
           f'You are a {profession}'
           f'You were in {affiliation}')
print (message)
# 'Hi Eric. You are a comedian. You were in Monty Python.'

# otherwise, use triple delimiters for newline printing
message = (f'''Hi {name}
You are a {profession}
You were in {affiliation}''')
print (message)
# Hi Eric
# You are a comedian
# You were in Monty Python

# f-strings are faster than either str.format() and %-format operator
import timeit
ampersand_time = timeit.timeit ("""name = 'Eric'
age = 74
'%s is %s.' % (name, age)""", number = 10000)
# 0.009556600009091198
format_time = timeit.timeit ("""name = 'Eric'
age = 74
'{} is {}.'.format(name, age)""", number = 10000)
# 0.01239339995663613
fstring_time = timeit.timeit ("""name = 'Eric'
age = 74
f'{name} is {age}.'""", number = 10000)
fstring_time = 3

print (f"{'ampersand_time':15}: time : {ampersand_time:.6f}s, ratio: {ampersand_time / fstring_time:.3}")  # ampersand_time : time : 0.009850s, ratio: 1.5
print (f"{'format_time':15}: time : {format_time:.6f}s, ratio: {format_time / fstring_time:.3}")  # format_time    : time : 0.011951s, ratio: 1.82
print (f"{'fstring_time':15}: time : {fstring_time:.6f}s, ratio: {fstring_time / fstring_time:.3}")  # fstring_time   : time : 0.006584s, ratio: 1.0

# f-String Expression Limitations:

# 1- f-string expression can’t have invalid spaceholders (braces empty of arguments):
# print(f'foo{}bar') # SyntaxError: f-string: empty expression not allowed

# 2- f-string can’t contain a backslash (\) character, which means you can’t escape sequences in f-string expressions
# print(f'foo{\'}bar') # SyntaxError: f-string expression part cannot include a backslash
# print(f'foo{\n}bar') # SyntaxError: f-string expression part cannot include a backslash
# can get around by creating a temporary variable that contains the escape sequence
nl = '\n'
print (f'foo{nl}bar')
# foo
# bar
quote = '\''
print (f'foo{quote}bar')  # foo'bar

# 3- a triple-quoted f-string can’t contain comments
# print (f'''[foo
# {z} # Comment
# baz]''')
# SyntaxError: f-string expression part cannot include '#'

# modified formatting:
print (f'{s!r}')  # 'bar'
# equivalent to
print ('{!r:}'.format (s))  # 'bar'

print (f'{s:*^8}')  # **bar***
# equivalent to
print ('{:*^8}'.format (s))  # **bar***

a = ['foo', 'bar', 'baz', 'qux', 'quux']
w = 4
print (f'{len (a):0{w}d}')  # 0005
# equivalent to
print ('{:0{}d}'.format (len (a), w))  # 0005

n = 123456788
sep = '_'
print (f'{n + 1:{sep}d}')  # 123_456_789
# equivalent to
print ('{:{}d}'.format (n + 1, sep))  # 123_456_789