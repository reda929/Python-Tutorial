from operator import attrgetter, itemgetter


# list.sort() modifies the list in-place, while sorted() builds a new sorted list
print(sorted([5, 2, 3, 1, 4]))  # [1, 2, 3, 4, 5]
# list.sort() modifies the list in-place, and is slightly more efficient
a = [5, 2, 3, 1, 4]
a.sort()
print(a)  # [1, 2, 3, 4, 5]
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))  # [1, 2, 3, 4, 5]
print(sorted("This is a test string from Andrew".split(), key = str.lower))  # ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# key is a function (or other callable) that takes a single argument and returns a key to use for sorting purposes

# can sort using some of the object’s indices as keys:
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ]
sorted(student_tuples, key = lambda student: student[2])  # sort by age  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]/

# can sort using some of the object’s indices as keys:
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ]
print(sorted(student_tuples, key = lambda student: student[0]))
print(sorted(student_tuples, key = lambda student: student[1]))
print(sorted(student_tuples, key = lambda student: student[2]))


# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# works for objects with named attributes as well:

class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10), ]
print(sorted(student_objects, key = lambda student: student.age))

# Operator Module Functions
# operator module has itemgetter(), attrgetter(), and a methodcaller() function.


print(sorted(student_tuples, key = itemgetter(2)))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(sorted(student_objects, key = attrgetter('age')))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# can sort on an attribute then on another, like to sort by grade then by age:
print(sorted(student_tuples, key = itemgetter(1, 2)))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
print(sorted(student_objects, key = attrgetter('grade', 'age')))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

# Ascending and Descending
print(sorted(student_tuples, key = itemgetter(2), reverse = True))  # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(student_tuples, key = itemgetter(2), reverse = False))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# sorted() sorts are guaranteed to be stable, i.e., when multiple records have the same key, their original order is preserved

data = [('a', 2), ('b', 2), ('a', 1), ('b', 1)]
print(sorted(data, key = itemgetter(0)))

# [('a', 2), ('a', 1), ('b', 2), ('b', 1)]

s = sorted(student_objects, key = attrgetter('age'))  # sort on secondary key
print(sorted(s, key = attrgetter('grade'), reverse = True))  # now sort on primary key, descending


# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# can be abstracted in a function that sorts lists on multiple passes

def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key = attrgetter(key), reverse = reverse)
    return xs


print(multisort(list(student_objects), (('grade', True), ('age', False))))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# First, the initial list is decorated with new values that control the sort order.
# Second, the decorated list is sorted.
# Finally, the decorations are removed, creating a list that contains only the initial values in the new order.
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
print(decorated)  # [('A', 0, ('john', 'A', 15)), ('B', 1, ('jane', 'B', 12)), ('B', 2, ('dave', 'B', 10))]
decorated.sort()
print([student for grade, i, student in decorated])  # undecorate

# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

# this works because tuples are compared lexicographically; the first items are compared; if they are the same then the second items are compared, and so on
# It is not strictly necessary in all cases to include the index i in the decorated list, but including it gives two benefits:
# ensure stability: if two items have the same key, their order will be preserved in the sorted list.
# The original items do not have to be comparable because the ordering of the decorated tuples will be determined by at most the first two items. So for example the original list could contain complex numbers which cannot be sorted directly