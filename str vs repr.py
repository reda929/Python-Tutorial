s = 'Hello, Geeks.'
print (str(s)) # 'Hello, Geeks.'
print (repr (s))  # ''Hello, Geeks.''
print (str(2.0/11.0)) # '0.181818181818'
print (repr(2.0/11.0))  #'0.18181818181818182'

# str() is used for creating output for end user
# str() is used to compute the “informal” string representation of an object (a representation that is useful for printing the object).
# repr() is mainly used for debugging and development
# repr() compute the “official” string representation of an object (from which we can reconstruct the object again)
# if we suspect a float has a small rounding error, str will round that number, while repr will show the exact value in the variable

# print() and str() use __str__ of the object
# repr() uses __repr__ instead

# example
import datetime


today = datetime.datetime.now ()

# end-user friendly
print (str (today))  # '2016-02-22 19:32:04.078030'
# dev/debugging oriented
print (repr (today))  # 'datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)'

# overriding __repr__ and __str__ attributes
class Student:

    def __init__ (self, name, id):
        self.name = name
        self.id = id


    def __str__ (self):
        return 'I am {student.name}, with ID #{student.id}'.format (student = self)

    def __repr__(self):
        return 'Student (\'{student.name}\', {student.id})'.format (student = self)
myStudent = Student ('Bryan', 1321)
print (myStudent)  # 'I am Bryan, with ID #1321'
print (str(myStudent))  # 'I am Bryan, with ID #1321'
print (repr (myStudent))  # 'Student ('Bryan', 1321)'