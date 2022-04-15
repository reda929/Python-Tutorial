# basic operations
print (25 + 4)  # 29
print (25 - 4)  # 21
print (25 * 4)  # 100
print (25 / 4)  # 6.25
print (3 ** 4)  # 81
print (25 % 4)  # 1
print (25 // 4)  # 6
print ()

# boolean operations
x = 3
y = 6
print (x < y) # True
print (x > y)  # False
print (2 * x <= y)  # True
print (2 * x >= y)  # True
print (2 * x == y)  # True
print (2 * x != y)  # False
print ()

# data type initiation
x = int (4.7)
y = float (4)
print(round (12.345, 2))
print (x)  # 4
print (y)  # 4.0

# read type
print (type (x))  # (<class 'int'>), i.e., int
print (type (y))  # (<class 'float'>), i.e., float.

# concatinating strings for constants only
print('Py' 'thon')
print ('Py'
       'thon')

# r-strings
# escapable characters are escaped
print('C:\some\name')
# escapable characters are not escaped
print(r'C:\some\name')

# multiple strings using triple-quotes: """, ''' as delimiters
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# floats are not exact
print (.1 + .1 + .1)  # 0.30000000000000004
print (.3)  # 0.3
print (.1 + .1 + .1 == .3)  # 0.3 != 0.30000000000000004