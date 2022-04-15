######################
# Regular Expression #
######################

# Regular expressions
# Use '\' to escape special characters literally: searching '\\' as a pattern is interpreted as a literal '\'
# Backslashes are not escaped in raw string notation:
# r"\n" is a combination of '\' and 'n' characters, while "\n" is a one-character string of a newline

#############################
# Regular Expression Syntax #
#############################

# Regular expression (RE) specifies a set of strings of special meaning to match for in a string.
# Instead of looking for literal 'abc', one can search for (ASCII characters ocurring 3 times) or (3 adjacent ASCII characters in consequent order, 'RST' would match this meaning too).
# REs are normal strings that are later compiled; so if A and B are both REs, then AB is also a RE.
# Generally speaking, if a string p matches A and another string q matches B, the string pq will match AB; but may not work if A or B contained a boundary conditions between A and B; or have numbered group references:
# For a = 'aa', b = 'bb', the regex (character 'a' then end of string) matches a (i.e., 'aa'), but no matter what regex b is, the regex (character 'a' then end of string) will not match ab (i.e., 'aabb').

# REs can contain both special and ordinary/literal characters:
# Generally, any character other than special character (like 'a', 'X', '3', '<' and other literals in languages). 'a' matches somewhere in 'ball', but \w (meaning a word character) matches every character in 'ball'
# Repetition qualifiers (*, +, ?, {m,n}, etc) cannot be directly nested. This avoids ambiguity with the non-greedy modifier suffix ?, and with other modifiers. To apply a second repetition to an inner repetition, parentheses may be used. For example, (?:a{6})* matches any multiple of six 'a'; notice the {} and * in RE.

import re
import string


# This file repeats for-loops many times.


def pmatch(ptr, str, flag = 0, ind = False):
    """
    ind: if True, prints the start and end indices
    """
    captured_groups = []
    matches = re.finditer(ptr, str, flag)
    found = False
    for m in matches:
        print(f'|{m.group(0)}|, start: {m.start()}, end: {m.end()}')
        captured_groups.append(m.groups())
        found = True
    if not found:
        print('No output')
    return captured_groups


word = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

# To match a special escape character literally, escape it with a '\', or enclose it inside a character class; To match a '|', escape it like '\|' or enclose it as in [|].
punc = string.punctuation
# Escaping special characters with '\':
pmatch('\|', punc, ind = True)  # ||| start: 0, end: 1

# Enclosing special characters with square brackets:
pmatch('[!]', word, ind = True)  # |!|  start: 0, end: 1
# Special enclosing cases:
pmatch('[\']', word, ind = True)  # |'|  start: 6, end: 7
pmatch('[[]', word, ind = True)  # |[|  start: 22, end: 23 # FutureWarning: Possible nested set at position 1
pmatch('[\\\]', word, ind = True)  # |\|  start: 23, end: 24
pmatch('[]]', word, ind = True)  # |]|  start: 24, end: 25
pmatch('[\^]', word, ind = True)  # |^|  start: 25, end: 26

# The special characters are:

# '.': Matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline

pmatch('.', 'ab -0.')
# |a|
# |b|
# | |
# |-|
# |0|
# |.|

# '^': Matches the start of the string, and in MULTILINE mode also matches immediately after each newline
pmatch('^', 'a', ind = True)
# || start: 0, end: 0

# '$': Matches the end of the string before the newline at the end of the string, and in MULTILINE mode also matches before a newline:

pmatch('$', 'a', ind = True)  # || start: 1, end: 1
pmatch('foo$', 'foo', ind = True)  # |foo| start: 0, end: 3
pmatch('foo$', 'foobar', ind = True)  # No output

# foo.$ in 'foo1\nfoo2\nfoo3\n' matches before the last newline normally ('foo3'), but matches before every newline in MULTILINE mode ('foo1', 'foo2' and 'foo3')
pmatch('foo.$', 'foo1\nfoo2\nfoo3\n', ind = True)  # |foo3| start: 10, end: 14
pmatch('foo.$', 'foo1\nfoo2\nfoo3\n', flag = re.MULTILINE, ind = True)
# |foo1| start: 0, end: 4
# |foo2| start: 5, end: 9
# |foo3| start: 10, end: 14

# '*': Matches RE 0 or as many repetitions as possible:
pmatch('ab*', 'a', ind = True)  # |a| start: 0, end: 1
pmatch('ab*', 'ab', ind = True)  # |ab| start: 0, end: 2
pmatch('ab*', 'abbb', ind = True)  # |abbb| start: 0, end: 4

# '+': Matches RE 1 or more as many repetitions as possible:
pmatch('ab+', 'a')  # No output
pmatch('ab+', 'ab')  # |ab|
pmatch('ab+', 'abbb')  # |abbb|

# '?': Matches RE 0 or 1 times:
pmatch('ab?', 'a')  # |a|
pmatch('ab?', 'ab')  # |ab|
pmatch('ab?', 'abbb')  # |ab|

# '*?', '+?', '??': The non greedy counterparts of '*', '+', and '?' qualifiers; to match the least number possible of characters
# The RE <.*> matches '<a> <b> <c>', matching as many characters as possible by RE, not just '<a>';
# While the RE <.*?> will match only '<a>'

pmatch('<.*?>', '<a> <b> <c>')
# |<a>|
# |<b>|
# |<c>|

# {m}: Specifies that RE has to occur at least m number of times; \w{2} will match 'ab' in 'abc', and 'ab' in 'ab', but 'a'

pmatch('\w{2}', 'abcde')
# |ab|
# |cd|

# {m,n}: Specifies that RE has to occur from m to n number of times (as many times as possible); \w{2,3} will match 'abc' in 'abcde', then 'de', consuming the first 3 characters

pmatch('\w{2,3}', 'abcde')
# |abc|
# |de|

# {m,n}?: Specifies that RE has to occur from m to n number of times, matching in a  non-greedy way; \w{2,3} will match 'ab' in 'abcde', consuming the first 2 characters, then 'de'

pmatch('\w{2,3}?', 'abcde')
# |ab|
# |cd|

# '\': Either escapes special characters (so you can match characters like '*', '?' literally), or signals a special sequence
# Note: backslashes are not escaped by default, unless an escapable character is in the match

pmatch(r'\\\w', '\\a\ \-', ind = True)
# |\a| start: 0, end: 2

# []: Used to indicate a set of characters.
word = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

pmatch('[edcba]', word)

# |a|
# |b|
# |c|
# |d|
# |e|

pmatch('[l-p]', word)

# |l|
# |m|
# |n|
# |o|
# |p|

pmatch('[l-p4-7]', word)

# |l|
# |m|
# |n|
# |o|
# |p|
# |l|
# |m|
# |n|
# |o|
# |p|
# |4|
# |5|
# |6|
# |7|

pmatch('[-dcu]', word)

# |c|
# |d|
# |u|
# |-|

pmatch('[dcu-]', word)

# |c|
# |d|
# |u|
# |-|

# Special characters lose their special meaning inside sets. For example, [(+*)] will match any of the literal characters '(', '+', '*', or ')'.

pmatch('[(+*)]', word)

# |(|
# |)|
# |*|
# |+|

# Character classes: set of characters defined in a class

# '^': Negates the set; matches all the characters that are not in the set.
# The caret has no special meaning if it’s not the first character in the set.

pmatch('[^^]', 'a^b')

# |a|
# |b|

pmatch('[^02ae]', 'abcde01234')

# |b|
# |c|
# |d|
# |1|
# |3|
# |4|

# '|': For A|B, where A and B are arbitrary REs or groups, creates a regular expression that will match either A or B
# Since a union of two REs or groups is an RE or a group, the union operation can be applied to an arbitrary number of REs or groups this way.
# The target string is scanned by REs from left to right;
# For A|B, once A matches, B will not be tested further, even if B would produce a longer overall match.
# In other words, the '|' operator is never greedy.

pmatch('ab|abc', 'abc')  # |ab|

# (RE): A capturing group: Matches RE, and retrieves the content be used later (either in the matching operation itself or outside it).

m = pmatch('(ab*)', 'a ab ab aba')
print(f'[{m}], ', end = '')

# |a|  start: 0, end: 1
# |ab|  start: 2, end: 4
# |ab|  start: 5, end: 7
# |ab|  start: 8, end: 10
# |a|  start: 10, end: 11
# [[('a',), ('ab',), ('ab',), ('ab',), ('a',)]],

# (?<extension>): Extension Notations:
# (?:RE): A non-capturing version of regular parentheses. Matches RE with a string, but the string is not retrieved.

m = pmatch('(?:a)(\w+)', 'a ab ab aba')
print(f'[{m}], ', end = '')

# |ab|  start: 2, end: 4
# |ab|  start: 5, end: 7
# |aba|  start: 8, end: 11
# [[('b',), ('b',), ('ba',)]],

# (?P<name>RE<RE definition>): Defines an RE to be later used in the pattern.
# A symbolic group is also a numbered group, just as if the group were not named.

####################################
# Way to Reference Captured Groups #
####################################

# In repl argument of re.sub()      \g<quote>
# \g<quote>
# \g<1>
# \1

# Context                          Way to reference it
# In the same pattern itself        (?P=quote) (as shown)
#                                   \1
#
# When processing match object m    m.group('quote')
#                                   m.end('quote') (etc.)
#
# In repl argument of re.sub()      \g<quote>
#                                   \g<1>
#                                   \1

# In the same pattern itself:
# (?P=<name>): A backreference to a named group, matching whatever was matched by group named name.

matches = re.finditer('((?P<myvar>[a-c])-(?P=myvar)) ', 'a-a b-b c-c e-e f-f g-g a-c ')
for m in matches:
    # print(m) # <re.Match object; span=(0, 4), match='a-a '>
    # continue
    print(f'|{m.group(0)}|', f' start: {m.start()}, end: {m.end()}')  # whole match ((?P<myvar>[a-c])-(?P=myvar))
    print(f'|{m.group(1)}|', f' start: {m.start()}, end: {m.end()}')  # first group (?P<myvar>[a-c])
    print(f'|{m.group(2)}|', f' start: {m.start()}, end: {m.end()}')  # second group (?P=myvar)
    break
# |a-a |  start: 0, end: 4
# |a-a|  start: 0, end: 4
# |a|  start: 0, end: 4

matches = re.finditer('((?P<myvar>[a-c])-(?P=myvar)) ', 'c-b ')
found = False
for m in matches:
    # print(m) # <re.Match object; span=(0, 4), match='a-a '>
    # continue
    found = True
    print(f'|{m.group(0)}|', f' start: {m.start()}, end: {m.end()}')  # whole match ((?P<myvar>[a-c])-(?P=myvar))
    print(f'|{m.group(1)}|', f' start: {m.start()}, end: {m.end()}')  # first group (?P<myvar>[a-c])
    print(f'|{m.group(2)}|', f' start: {m.start()}, end: {m.end()}')  # second group (?P=myvar)
    break
print('No Output' if not found else '')

# No Output

# \1
matches = re.finditer('([a-c])-\\1', 'a-a b-b c-c e-e f-f g-g ')
for m in matches:
    # print(m) # <re.Match object; span=(0, 3), match='a-a'>
    # continue
    print(f'|{m.group(0)}|', f' start: {m.start()}, end: {m.end()}')  # whole match |([a-c])-\\1|, where \1 is the first captured group, i.e., [a-c]
    print(f'|{m.group(1)}|', f' start: {m.start()}, end: {m.end()}')  # first group |([a-c])|
    break
# |a-a|  start: 0, end: 3
# |a|  start: 0, end: 3

matches = re.finditer('((?P<myvar>[a-c])-(?P=myvar)) ', 'a-a b-b c-c e-e f-f g-g a-c ')
for m in matches:
    print(f"m.group('myvar'): {m.group('myvar')}\n"
          f"m.start('myvar'), m.end('myvar'): [{m.start('myvar')}, {m.end('myvar')}]\n")

# m.group('myvar'): a
# m.start('myvar'), m.end('myvar'): [0, 1]
#
# m.group('myvar'): b
# m.start('myvar'), m.end('myvar'): [4, 5]
#
# m.group('myvar'): c
# m.start('myvar'), m.end('myvar'): [8, 9]

# In repl argument of re.sub():
# \g<name>

print('|' + re.sub('(?P<myvar>[a-c])-(?P=myvar) ', '\g<myvar>' * 5, 'a-a b-b c-c e-e f-f g-g ') + '|')
# |aaaaabbbbbccccce-e f-f g-g |

# \g<1>
print('|' + re.sub('(?P<myvar>[a-c])-(?P=myvar) ', '\g<1>' * 5, 'a-a b-b c-c e-e f-f g-g ') + '|')
# |aaaaabbbbbccccce-e f-f g-g |

# \1
print('|' + re.sub('([a-c])-\\1 ', '\\1' * 5, 'a-a b-b c-c e-e f-f g-g ') + '|')

# |aaaaabbbbbccccce-e f-f g-g |

# (?#...): A comment; the contents of the parentheses are simply ignored.
pmatch('ab|abc(?# This has no effect.)', 'abc')

# |ab|  start: 0, end: 2

# Lookahead Assertions: Matches if the current position in the string is or is not followed by a match for RE.

# (?=RE): Positive Lookahead Assertions; Matches if RE matches next, but doesn’t consume any of the string.

pmatch('a(?=\d)', 'a1 a- a. a-1 a.1 a2')

# |a|  start: 0, end: 1
# |a|  start: 17, end: 18

# (?!RE): Negative Lookahead Assertion; Matches if RE doesn't match next, but doesn’t consume any of the string.

pmatch('a(?!\d)', 'a1 a- a. a-1 a.1 a2')

# |a|  start: 3, end: 4
# |a|  start: 6, end: 7
# |a|  start: 9, end: 10
# |a|  start: 13, end: 14

# Lookahead Assertions: Matches if the current position in the string is or is not preceded by a match for RE
# Lookbehind Assertions require a fixed-width pattern

# (?<=RE): Positive Lookbehind Assertion; Matches if the current position in the string is preceded by a match for RE
# abc or a|b are allowed, but a* and a{3,4} are not.

# pmatch('(?<=a*)def', 'abc-def abcdef bcdef') # re.error: look-behind requires fixed-width pattern
pmatch('(?<=abc)def', 'abc-def abcdef bcdef')

# |def|  start: 11, end: 14

# This example looks for the hyphenated part of a word:

pmatch('(?<=-)\w+', 'abc-def abcdef bcdef math-wise')

# |def|  start: 4, end: 7
# |wise|  start: 26, end: 30

# (?<!RE): Negative Lookbehind Assertion; Matches if the current position in the string is not preceded by a match for RE.

pmatch('(?<!abc)def', 'abc-def abcdef bcdef')

# |def|  start: 4, end: 7
# |def|  start: 17, end: 20

# (?(id/name)yes-pattern|no-pattern)
# Will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t. no-pattern is optional and can be omitted. For example,
# (<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$) is a poor email matching pattern, which
# will match with '<user@host.com>' as well as 'user@host.com',
# but not with '<user@host.com' nor 'user@host.com>'.
# TODO

pmatch('(<)?a(?(1)|b)', '<a>')
pmatch('(<)?a(?(1)|b)', '<ab>')
pmatch('(<)?a(?(1)|b)', '<a>b')

# |<a|  start: 0, end: 2    |<a|  start: 0, end: 2
# |<a|  start: 0, end: 2    |<a|  start: 0, end: 2
# |<a|  start: 0, end: 2    |<a|  start: 0, end: 2

pmatch('(<)?a(?(1)|b)', '<a')
pmatch('(<)?a(?(1)|b)', '<ab')

# |<a|  start: 0, end: 2    |<a|  start: 0, end: 2
# |<a|  start: 0, end: 2    |<a|  start: 0, end: 2

pmatch('(<)?a(?(1)|b)', 'a>')
pmatch('(<)?a(?(1)|b)', 'ab>')
pmatch('(<)?a(?(1)|b)', 'a>b')

# No output                 |a|  start: 0, end: 1
# |ab|  start: 0, end: 2    |a|  start: 0, end: 1
# No output                 |a|  start: 0, end: 1

pmatch('(<)?a(?(1)|b)', 'a')
pmatch('(<)?a(?(1)|b)', 'ab')

# pmatch('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', '<user@host.com>')  # |<user@host.com>|  start: 0, end: 15
# pmatch('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', '<user@host.com')  # |user@host.com|  start: 1, end: 14
# pmatch('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', 'user@host.com>')  # No output
# pmatch('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', 'user@host.com')  # |user@host.com|  start: 0, end: 13

# The special sequences consist of '\' and a character from the list below.

# \<number from 1 to 99>: Matches the contents of the group of the same number.
# If the first digit of number is 0, or number is 3 octal digits long, it will not be interpreted as a group match, but as the character with octal value number.

pmatch('(\w+) \\1', 'the the')  # |the the|  start: 0, end: 7
pmatch('(\w+) \\1', '55 55')  # |55 55|  start: 0, end: 5
pmatch('(\w+) \\1', 'thethe')  # No output

# \A: Matches only at the start of the string. (Perhaps the same as ^)
pmatch('(\A)a', 'abc')  # |a|  start: 0, end: 1

# \b: Matches a word boundary; a boundary between a \w and either (a \W character or the beginning/end of the string).

pmatch(r'\bfoo\b', 'foo')  # |foo|  start: 0, end: 3
pmatch(r'\bfoo\b', 'foo.')  # |foo|  start: 0, end: 3
pmatch(r'\bfoo\b', '(foo)')  # |foo|  start: 1, end: 4
pmatch(r'\bfoo\b', 'bar foo baz')  # |foo|  start: 4, end: 7
pmatch(r'\bfoo\b', 'foobar')  # No output
pmatch(r'\bfoo\b', 'foo3')  # No output

# \B: Matches the empty string, but only when it is not at the beginning or end of a word. In other words, what's before and after \B is a word character.
# \B is just the opposite of \b.

pmatch(r'foo\B', 'foo')  # No output
pmatch(r'foo\B', 'foo,')  # No output
pmatch(r'foo\B', 'foo.')  # No output
pmatch(r'foo\B', '(foo)')  # No output
pmatch(r'foo\B', 'bar foo baz')  # No output
pmatch(r'foo\B', 'foobar')  # |foo|  start: 0, end: 3
pmatch(r'foo\B', 'foo3')  # |foo|  start: 0, end: 3
pmatch(r'py\B', 'python')  # |py|  start: 0, end: 2

# \d: Matches any Unicode decimal digit, i.e., character class [0-9].
pmatch(r'\d', 'abc 123')

# |1|  start: 4, end: 5
# |2|  start: 5, end: 6
# |3|  start: 6, end: 7

# \D: Matches any character that is not Unicode decimal digit; The opposite of \d, or [^0-9].
pmatch(r'\D', 'abc 123')

# |a|  start: 0, end: 1
# |b|  start: 1, end: 2
# |c|  start: 2, end: 3
# | |  start: 3, end: 4

# \s: Matches Unicode whitespace characters ([ \t\n\r\f\v]).
pmatch(r'\s', 'abc 123,.!()\t\n\r\f\v')

# | |  start: 3, end: 4
# |	|  start: 12, end: 13
# |
# |  start: 13, end: 14
# |  start: 14, end: 15
# ||  start: 15, end: 16
# ||  start: 16, end: 17

# \S: Matches any character that is not Unicode whitespace character ([^ \t\n\r\f\v]); The opposite of \s.

pmatch(r'\S', 'abc 123,.!()\t\n\r\f\v')

# |a|  start: 0, end: 1
# |b|  start: 1, end: 2
# |c|  start: 2, end: 3
# |1|  start: 4, end: 5
# |2|  start: 5, end: 6
# |3|  start: 6, end: 7
# |,|  start: 7, end: 8
# |.|  start: 8, end: 9
# |!|  start: 9, end: 10
# |(|  start: 10, end: 11
# |)|  start: 11, end: 12

# \w: Matches Unicode word characters; including letters, digits and underscore: only [a-zA-Z0-9_].
pmatch(r'\w', 'abc 123,.!()\t\n\r\f\v')

# |a|  start: 0, end: 1
# |b|  start: 1, end: 2
# |c|  start: 2, end: 3
# |1|  start: 4, end: 5
# |2|  start: 5, end: 6
# |3|  start: 6, end: 7

# \W: Matches any character that is not Unicode word characters; This is the opposite of \w, or [^a-zA-Z0-9_].
pmatch(r'\W', 'abc 123,.!()\t\n\r\f\v')

# | |  start: 3, end: 4
# |,|  start: 7, end: 8
# |.|  start: 8, end: 9
# |!|  start: 9, end: 10
# |(|  start: 10, end: 11
# |)|  start: 11, end: 12
# |	|  start: 12, end: 13
# |
# |  start: 13, end: 14
# |  start: 14, end: 15
# ||  start: 15, end: 16
# ||  start: 16, end: 17

# \Z: Matches only at the end of the string. (Perhaps the same as $)

pmatch(r'\Z', 'abc 123,.!()\t\n\r\f\v')

# ||  start: 17, end: 17
"""
###########################################
###########################################
"""
# Module Contents:
# re.compile(pattern, flags=0): Compiles a regular expression pattern into a regular expression object, which can be used for other functions.

# The expression’s behaviour can be modified by specifying a flags value. Values can be any of the following variables, combined using bitwise OR (the | operator).

# The sequence
# prog = re.compile(pattern)
# result = prog.match(string)

# is equivalent to
# result = (re.compile(pattern)).match(string)

# is equivalent to
# result = re.match(pattern, string)

# but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.

# re.DEBUG
# Display debug information about compiled expression. No corresponding inline flag.

# re.I
# re.IGNORECASE: Matches are case-insensitive; expressions like [A-Z] will also match lowercase letters.

# re.M
# re.MULTILINE
# When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline). By default, '^' matches only at the beginning of the string, and '$' only at the end of the string and immediately before the newline (if any) at the end of the string. Corresponds to the inline flag (?m).

# '$': Matches the end of the string before the newline at the end of the string, and in MULTILINE mode also matches before a newline:
pmatch('$', 'a', ind = True)  # ||  start: 1, end: 1
pmatch('foo$', 'foo', ind = True)  # |foo|  start: 0, end: 3
pmatch('foo$', 'foobar', ind = True)  # No output

# foo.$ in 'foo1\nfoo2\nfoo3\n' matches before the last newline normally ('foo3'), but matches before every newline in MULTILINE mode ('foo1', 'foo2' and 'foo3')
pmatch('foo.$', 'foo1\nfoo2\nfoo3\n', ind = True)  # |foo3|  start: 10, end: 14
pmatch('foo.$', 'foo1\nfoo2\nfoo3\n', flag = re.MULTILINE, ind = True)

# |foo1|  start: 0, end: 4
# |foo2|  start: 5, end: 9
# |foo3|  start: 10, end: 14

pmatch('^', 'a', ind = True)  # ||  start: 0, end: 0
pmatch('^foo', 'foo', ind = True)  # |foo|  start: 0, end: 3
pmatch('^foo', 'foobar', ind = True)  # |foo|  start: 0, end: 3

# ^foo. in 'foo1\nfoo2\nfoo3\n' matches before the first newline normally ('foo1'), but matches before every newline in MULTILINE mode ('foo1', 'foo2' and 'foo3')
pmatch('^foo.', 'foo1\nfoo2\nfoo3\n', ind = True)  # |foo1|  start: 0, end: 4
pmatch('^foo.', 'foo1\nfoo2\nfoo3\n', flag = re.MULTILINE, ind = True)

# |foo1|  start: 0, end: 4
# |foo2|  start: 5, end: 9
# |foo3|  start: 10, end: 14

# re.S
# re.DOTALL: Makes '.' match any character at all, including a newline; otherwise, '.' will match anything except a newline.

# re.X
# re.VERBOSE: Allows regular expressions to be put in a more readable format as in regular code, including comments.
# Whitespace within the pattern is ignored, except in a character class, or when preceded by an unescaped backslash, or within tokens like *?, (?: or (?P<...>.

a = re.compile(r"""\d +  # the integral part
                    \.    # the decimal point
                    \d *  # some fractional digits""", re.X)
print(a.match('1'))  # None
print(a.match('1.1'))  # <re.Match object; span=(0, 3), match='1.1'>
print(a.match('.1'))  # None
print(a.match('1.'))  # <re.Match object; span=(0, 2), match='1.'>

# Equivalent to:
a = re.compile(r'\d+\.\d*')

a = re.compile(r'\w\ ', re.X)
print(a.match('a'))  # None
print(a.match('a '))  # <re.Match object; span=(0, 2), match='a '>
print(a.match(' a'))  # None
print(a.match(' a '))  # None

# TODO
# re.search(pattern, string, flags=0): Matches pattern on string, returning the first match.
matches = re.search('\w*', 'abc 123')
print(matches)

# <re.Match object; span=(0, 3), match='abc'>

# TODO
# re.match(pattern, string, flags=0)
# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern; note that this is different from a zero-length match.
matches = re.match('\w*', 'abc 123')
print(matches)

# <re.Match object; span=(0, 3), match='abc'>

# re.split(pattern, string, maxsplit=0, flags=0): Returns a list of strings split by matching pattern on string.
# If capturing parentheses are used in pattern, the text of all groups are also returned in the list.
# If number of matchings exceeded maxsplit, remainder of the string is returned as the final element of the list.
# That way, separator components are always found at the same relative indices within the result list.

print(re.split(r'\W+', 'a, b, c'))  # ['a', 'b', 'c']
print(re.split(r'(\W+)', 'a, b, c'))  # ['a', ', ', 'b', ', ', 'c']
print(re.split(r'\W+', 'a, b, c', 1))  # ['a', 'b, c']
print(re.split(r'\W+', 'A, b, C', flags = re.IGNORECASE))  # ['A', 'b', 'C']
print(re.split(r'(\W)', '.a, b.'))  # ['', '.', 'a', ',', '', ' ', 'b', '.', '']
print(re.split(r'\b', 'a, b, c.'))  # ['', 'a', ', ', 'b', ', ', 'c', '.']
print(re.split(r'\W', '.a.'))  # ['', 'a', '']
print(re.split(r'(\W)', '.a.'))  # ['', '.', 'a', '.', '']

# re.findall(pattern, string, flags=0): Returns all non-overlapping matches (scanned left-to-right) of pattern in string, as a list of strings or tuples (returned in the same order matches were found).
# The string is scanned left-to-right, and matches are returned in the order found.
# Empty matches are included in the result.

# The result depends on the number of capturing groups in the pattern.
# If there are no groups, return a list of strings matching the whole pattern.
# If there is exactly one group, return a list of strings matching that group.
# If multiple groups are present, return a list of tuples of strings matching the groups.
# Non-capturing groups do not affect the form of the result.

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # ['foot', 'fell', 'fastest']
print(re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10'))  # [('width', '20'), ('height', '10')]

# re.finditer(pattern, string, flags=0): Returns all non-overlapping matches (scanned left-to-right) of pattern in string, as a list of strings or tuples (returned in the same order matches were found).
# The string is scanned left-to-right, and matches are returned in the order found.
# Empty matches are included in the result.

for i in re.finditer(r'\bf[a-z]*', 'which foot or hand fell fastest'):
    print(i)

# <re.Match object; span=(6, 10), match='foot'>
# <re.Match object; span=(19, 23), match='fell'>
# <re.Match object; span=(24, 31), match='fastest'>

for i in re.finditer(r'(\w+)=(\d+)', 'set width=20 and height=10'):
    print(i)

# <re.Match object; span=(4, 12), match='width=20'>
# <re.Match object; span=(17, 26), match='height=10'>

# re.sub(pattern, repl, string, count=0, flags=0):
# Returns the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.
# If pattern isn’t found, string is returned unchanged.
# repl can be a string or a function; Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern.
# count is the maximum number of pattern occurrences to be replaced.
print(re.sub('abc(\d+)', '\\1', 'abc abc123 123 abc'))  # abc 123 123 abc
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags = re.IGNORECASE))  # Baked Beans & Spam

# Empty matches for the pattern are replaced only when not adjacent to a previous empty match:
print(re.sub('b*', '-', 'abc'))  # -a--c-

# re.subn(pattern, repl, string, count=0, flags=0)
# Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).
print(re.subn('b*', '-', 'abc'))  # ('-a--c-', 4)

# re.escape(pattern): Escapes characters which have a special meaning in Python's REs in pattern.
# Note that those character are not the same as escapable characters.

print(re.escape('https://www.python.org'))
# https://www\.python\.org

legal_chars = string.punctuation
print(f'Original characters: [{legal_chars}]\n'
      f'RE escaped characters: [{re.escape(legal_chars)}]')

# Original characters: [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
# RE escaped characters: [!"\#\$%\&'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}\~]

"""
###########################################
###########################################
"""

# Match.start([group])
# Match.end([group]): Returns the indices of the start and end of the substring matched by group; group defaults to zero (meaning the whole matched substring).

# Matches can be references by order of occurrence, or name defined in pattern:

# Referencing matches by order of occurrence:
matches = re.finditer('(\w+) (\w+) (\w+)', 'abc de fgehi')
for m in matches:
    print(f"Whole match:|{m.group(0) + '|':15}, start: {m.start(0)}, end: {m.end(0)}")
    print(f"1st match:  |{m.group(1) + '|':15}, start: {m.start(1)}, end: {m.end(1)}")
    print(f"2nd match:  |{m.group(2) + '|':15}, start: {m.start(2)}, end: {m.end(2)}")
    print(f"3rd match:  |{m.group(3) + '|':15}, start: {m.start(3)}, end: {m.end(3)}")

# Whole match:|abc de fgehi|  , start: 0, end: 12
# 1st match:  |abc|           , start: 0, end: 3
# 2nd match:  |de|            , start: 4, end: 6
# 3rd match:  |fgehi|         , start: 7, end: 12

# i.e., m.group(g) is equivalent to m.string[m.start(g):m.end(g)]

# Referencing matches by name defined in pattern:
matches = re.finditer('(\w+) (?P<someword>\w+) (\w+)', 'abc de fgehi')
for m in matches:
    print(f"'someword' match:|{m.group('someword') + '|':15}, start: {m.start('someword')}, end: {m.end('someword')}")

# 'someword' match:|de|            , start: 4, end: 6

# Match.groups(default=None): Returns a tuple containing all the subgroups of the match.

matches = re.finditer('(\w+) (?P<someword>\w+) (\w+)', 'abc de fgehi')
for m in matches:
    print(m.groups())

# ('abc', 'de', 'fgehi')

# Match.groupdict(default=None): Returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.

matches = re.finditer('(\w+) (?P<someword>\w+) (\w+)', 'abc de fgehi')
for m in matches:
    print(m.groupdict())

# {'someword': 'de'}