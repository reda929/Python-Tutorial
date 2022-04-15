a = 42
b = 47


def func ():
    return 5


# enquiring for local variables values in scope
print (locals ())  # '{'a': 42, 'b': 47, 'func': <function later.<locals>.func at some_address>}'
# print(*objects, sep=’ ’, end=’\n’, file=sys.stdout, flush=False)

print ('foo', 42, 'bar')  # 'foo 42 bar'
print ('foo', 42, 'bar', sep = '-')  # 'foo-42-bar'
# squishing output with '' for sep
print ('foo', 42, 'bar', sep = '')  # 'foo42bar'
# modified end character
print ('foo', end = '/')
print (42, end = '/')
print ('bar')
# foo/42/bar

print ('list printing:')
list = [100.768945, 17.232999, 60.98867, 300.837487]
output = ['{:.2f}'.format (elem) for elem in list]
print (output)

dictionary = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in dictionary.items ():
    print (k, v, sep = ' -> ')
# foo -> 1
# bar -> 2
# baz -> 3

print ('dict unpacking:')

# way 1:
for k in dictionary:
    print ('{key}: {value}'.format (key = k, value = dictionary[k]))

# way 2:
for k in dictionary:
    format_string = k + ': {' + k + '}'  # foo: {foo}
    print (format_string.format (**dictionary))
# foo: 1
# bar: 2
# baz: 3
# or
print ('{}{}{}'.format (**dictionary))