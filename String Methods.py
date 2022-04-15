# string methods
s = "Python"
print ('|' + s.center (10) + '|')  # '  Python  '
print ('|' + s.center (10, "*") + '|')  # '**Python**'
print ('|' + s.ljust (10) + '|')  # '|Python    |'
print ('|' + s.ljust (10, "*") + '|')  # '|Python****|'
print ('|' + s.rjust (10) + '|')  # '|    Python|'
print ('|' + s.rjust (10, "*") + '|')  # '|****Python|'
print ('|' + s.zfill (10) + '|')  # '|0000Python|'

text = 'aAa AaA AaAaA 123'

# str.upper(): Returns a string with all cased characters uppercased
print (text.upper ())  # AAA AAA AAAAA 123

# str.lower(): Returns a string with all cased characters lowercased
print (text.lower ())  # aaa aaa aaaaa 123

# str.capitalize(): Returns a string with its first character capitalized and the rest lowercased.
print (text.capitalize ())  # Aaa aaa aaaaa 123

# str.swapcase(): Returns a string with uppercase characters lowercased, and vice versa
# Note that it is not necessarily true that s.swapcase().swapcase() == s.
print (text.swapcase ())  # AaA aAa aAaAa 123

# str.title(): Returns a titlecased string where every word start with an uppercase character and the remaining characters are lowercase
print (text.title ())  # Aaa Aaa Aaaaa 123
# apostrophes form a word boundary, as in contractions and possessives form, which may not be the desired result
print ("they're bill's friends from the UK".title ())  # They'Re Bill'S Friends From The Uk
# A workaround for apostrophes can be constructed using regular expressions:
import re
def titlecase (s):
    return re.sub (r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group (0)[0].upper () + mo.group (0)[1:].lower (), s)
print (titlecase ("they're bill's friends."))  # "They're Bill's Friends.")

# str.center(width[, fillchar]): Returns centered string in a length width, with fillchar (default is an ASCII space) padding the rest of field width
# original string is returned if width is less than or equal to len(s).
print ('|{}|'.format(text.center (11)))
print ('|{}|'.format (text.center (11, '.')))
print ('|{}|'.format (text.center (12)))
print ('|{}|'.format (text.center (12, '.')))
print ('|{}|'.format (text.center (13)))
print ('|{}|'.format (text.center (13, '.')))

# str.count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of substring sub in the range [start, end]
print(text.count ('AaA'))

# str.startswith(prefix[, start[, end]]): Returns True if string starts with prefix, False otherwise
# prefix can also be a tuple of prefixes to look for any of them.
print (text.startswith ('aA')) # True
print (text.startswith ('ab'))  # False
print (text.startswith (('ab', 'aA')))  # True 

# str.endswith(suffix[, start[, end]]): Returns True if string ends with suffix, False otherwise
# suffix can also be a tuple of suffixes to look for any of them.
print (text.endswith ('AaA'))  # False
print (text.endswith ('123'))  # True
print (text.endswith (('AaA', '123')))  # True

# str.expandtabs(tabsize=8): Returns a string where all tab characters are replaced by one or more spaces
# view can vary, and shown text on console might not reflect exactly 8 spaces, but output is
print ('1\t2\t3\t4') # '1	2	3	4'
print ('1\t2\t3\t4'.expandtabs ()) # '1       2       3       4'
print ('1\t2\t3\t4'.expandtabs (4)) # '1   2   3   4'
print ('1\t2\t3\t4'.expandtabs (8)) # '1       2       3       4'

# str.find(sub[, start[, end]]): Returns the lowest index in the string where substring sub is found within the slice s[start:end]. Returns -1 if sub is not found.
print (text.find ('AaA')) # 4

# str.rfind(sub[, start[, end]]): Returns the highest index in the string where substring sub is found within the slice s[start:end]. Returns -1 if sub is not found.
print(text.rfind('123')) # 14

# str.rindex(sub[, start[, end]]): Like rfind() but raises ValueError when the substring sub is not found.
print (text.rindex ('123'))  # 14    
# If you need to know if string contains substring, in operator is better than find() :
print('AaA' in text)

# str.index(sub[, start[, end]]): same as find(), but raises ValueError if substring was not found
print (text.index ('AaA'))

# str.format(*args, **kwargs): Performs a string formatted as per defined by replacement field and arguments associated.
print("The sum of 1 + 2 is {0}".format (1 + 2)) # 'The sum of 1 + 2 is 3'

# str.isalnum(): Returns true if all characters are alphanumeric, and #str >= 1, false otherwise.
print (text.replace (' ', '').isalnum ())

# str.isalpha(): Returns true if all characters are alphabetic, and #str >= 1, false otherwise.
print ('aAa'.isalpha ())

# str.isdecimal(): Returns true if all characters are decimal characters, and #str >= 1, false otherwise.
print ('12'.isdecimal ())

# str.isidentifier(): Returns true if the string is a valid identifier according to the language definition. Use
print ('myVariable'.isidentifier ())

# str.isupper(): Returns true if all cased characters are uppercase and there is at least one cased character, false otherwise.
print ('AAA'.isupper ())

# str.islower(): Returns true if all cased characters are lowercase and there is at least one cased character, false otherwise.
print('aaa'.islower ())

# str.isspace(): Returns true if there are only whitespace characters in the string and #str >= 1, false otherwise.
print (' '.isspace ())

# str.istitle(): Returns True if the string is a titlecased string and #str >= 1, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Returns False otherwise.
print ('Thissentence'.istitle ())

# str.join(iterable): Returns a string concatenation of iterable, with separator = str
print ('-'.join (['a', 'b', 'c']))

# str.ljust(width[, fillchar]): Returns the string left justified in width field, padding rest of field with fillchar (default is ' '). Returns original string if width is <= len(s)
print ('|{}|'.format (text.ljust (19, '*')))

# str.rjust(width[, fillchar]): Returns the string right justified in width field, padding rest of field with fillchar (default is ' '). Returns original string if width is <= len(s)
print ('|{}|'.format (text.rjust (19, '*')))

# str.strip([chars]): Returns a string with leading and trailing chars string characters removed (default is ' '). The chars argument is not a prefix; rather, all combinations of its values are stripped:
print ('|{}|'.format ('   spacious   '.strip ()))  # |spacious|
print ('|{}|'.format ('www.example.com'.strip ('cmowz.')))  # |example|
print ('|{}|'.format ('#....... Section 3.2.1 Issue #32 .......'.strip ('.#! ')))  #|Section 3.2.1 Issue #32|

# str.lstrip([chars]): Returns a string with leading chars string characters removed (default is ' '). The chars argument is not a prefix; rather, all combinations of its values are stripped:
print ('|{}|'.format ('   spacious   '.lstrip ()))  # |spacious   |
print ('|{}|'.format ('aababa bab'.lstrip ('ab')))  # | bab|
print ('|{}|'.format (' aababa bab '.lstrip ('ab')))  # | aababa bab |
# notice space is omitted from removal

# str.rstrip([chars]): Returns a string with trailing chars string characters removed (default is ' '). The chars argument is not a prefix; rather, all combinations of its values are stripped:
print ('|{}|'.format ('   spacious   '.rstrip ()))  # |   spacious|
print ('|{}|'.format ('aababa bab'.rstrip ('ab')))  # |aababa |
print ('|{}|'.format (' aababa bab '.rstrip ('ab')))  # | aababa bab |

# str.partition(sep): Splits the string at the first occurrence of sep into a 3-tuple (before_sep, sep, after_sep).
# If the separator is not found, (str, '', '') is returned
print ('a-b-c'.partition ('-')) # ('a', '-', 'b-c')
print ('a-b-c'.partition (' '))  # ('a-b-c', '', '')

# str.rpartition(sep): Splits the string at the last occurrence of sep into a 3-tuple (before_sep, sep, after_sep).
# If the separator is not found, ('', '', str) is returned
print ('a-b-c'.rpartition ('-'))  # ('a-b', '-', 'c')
print ('a-b-c'.rpartition (' '))  # ('', '', 'a-b-c')

# str.replace(old, new[, count])
# Returns a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
brackets = '[[[]'
print ('|{}|'.format(brackets))  # |[[[]|
brackets = brackets.replace ('[]', ']', 1)
print ('|{}|'.format (brackets))  # |[[]|
brackets = brackets.replace ('[]', ']', 1)
print ('|{}|'.format (brackets))  # |[]|
brackets = brackets.replace ('[]', ']', 1)
print ('|{}|'.format (brackets))  # |]|
print ('|{}|'.format ('[[[]]]'.replace ('[]', '')))  # |[[]]|


# str.removesuffix(suffix, /): removes the suffix string from the end, otherwise, return a copy of the original string

print('MiscTests'.removesuffix('Tests'))  # 'Misc'
print('TmpDirMixin'.removesuffix('Tests'))  # 'TmpDirMixin'


# str.split(sep=None, maxsplit=-1): Returns a list of strings split by sep string from the left side, at most maxsplit number of times (with at most maxsplit+1 elements) (default to most possible number of splits)
# consecutive occurence of string sep are not grouped together into one string, instead they result in empty strings ('1,,2'.split(',') returns ['1', '', '2'])
print('1,2,3'.split (',')) # ['1', '2', '3']
print('1,2,3'.split (',', maxsplit = 1)) # ['1', '2,3']
print('1,2,,3,'.split (',')) # ['1', '2', '', '3', '']
# If sep is not specified or is None, the result will contain no empty strings (as if the string was trimmed of whitespaces
print('1 2 3'.split ()) # ['1', '2', '3']
print('1 2 3'.split (maxsplit = 1)) # ['1', '2 3']
print('  1  2  3  '.split ()) # ['1', '2', '3'] and not ['', '', '1', '', '', '2', '', '', '3', '', '']

# str.rsplit(sep=None, maxsplit=-1): Returns a list of strings split by sep string from the right side, at most maxsplit number of times (with at most maxsplit+1 elements) (default to most possible number of splits)
# consecutive occurence of string sep are not grouped together into one string, instead they result in empty strings ('1,,2'.rsplit(',') returns ['1', '', '2'])
print ('1,2,3'.rsplit (','))  # ['1', '2', '3']
print ('1,2,3'.rsplit (',', maxsplit = 1))  # ['1,2', '3']
print ('1,2,,3,'.rsplit (','))  # ['1', '2', '', '3', '']

# str.splitlines([keepends]): Returns a paragraph-like list of the lines, ending with line boundaries (which are not included in the list unless keepends is true). keepends  = [\n|\r]
print ('ab c\n\nde fg\rkl\r\n'.splitlines ())  # ['ab c', '', 'de fg', 'kl']
print ('ab c\n\nde fg\rkl\r\n'.splitlines (keepends = True))  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
# Unlike split() when a delimiter string sep is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line:
print ("".splitlines ())  # []
print ("One line\n".splitlines ())  # ['One line']
# For comparison, split('\n') gives:
print (''.split ('\n'))  # ['']
print ('Two lines\n'.split ('\n'))  # ['Two lines', '']