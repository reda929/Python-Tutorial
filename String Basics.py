a = 'a'
b = 'b'
n = 5
print (a + b)  # 'ab'
print (a * n)  # 'aaaaa'
print (len (a * n))  # 5
exit ()


def string_constants ():
    print ('can print any group')
    print ('String constants:')
    print ('\tstring.ascii_letters: ascii_lowercase, ascii_uppercase')
    print ('\tstring.ascii_lowercase: |abcdefghijklmnopqrstuvwxyz|')
    print ('\tstring.ascii_uppercase: |ABCDEFGHIJKLMNOPQRSTUVWXYZ|')
    print ('\tstring.digits: |0123456789|')
    print ('\tstring.hexdigits: |0123456789abcdefABCDEF|')
    print ('\tstring.octdigits: |01234567|')
    print ('\tstring.punctuation: |!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~| (without spaces)')
    print ('\tstring.printable: |digits, ascii_letters, punctuation, whitespace|')
    print ('\tstring.whitespace: |space, tab, linefeed, return, formfeed, vertical tab.f|')
    pass


def string_input ():
    # returns string until Enter key is pressed
    name = input ()
    print ('you typed: ', name)

    # prompts user for input with a message
    name = input ('This is a user input prompt')
    print ('you typed: ', name)

# string_constants ()
# string_input ()
