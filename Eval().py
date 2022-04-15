##########################
# EVALUATING EXPRESSIONS #
##########################

# eval(expression[, globals[, locals]]): runs the string representing a valid Python expression and optional globals (dictionary) and locals (a mapping object and could be dictionaries)
# eval() does not accept keyword arguments, eval(expression, locals={'x': 100})
# unless global and local dictionaries are provided, default contain a __builtins__ dictionary reference, ensuring eval() will have full access to all Python’s built-in names

# eval() can only evaluate expressions (pieces of code that evaluate to a value); so you cannot run statements like def, class, if, while, for, import, or assign value in eval() expressions

# WARNING: Untrusted User Input
# the user can have access to unintended resources like reading from a file on operating system, or run dangerous commands like writing on a file or deleting files on server

# eval() does not accept keyword arguments; next code is invalid:
# eval(expression, locals={'x': 100}) # TypeError: eval() takes no keyword arguments
# if locals' dictionary is to be used, globals' dictionary needs to be defined first (even if was empty):
# print(eval(expression, {}, {'x': 100})) # x = 100

x = 100
y = 200

# eval (expression): expression is executed with current scope's global and local names:
print (eval ('x + y'))  # 300

print (eval ('dir()'))  # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x', 'y']

# overriding __builtins__ dictionary
print (eval ('3 + 2 * 5 ** 2', {'__builtins__': None}))  # 53 # simple mathematical expressions are compiled

# eval() can't access names undefined in its dictionaries
# print (eval ('pow(3, 2)', {'__builtins__': None})) # built-in, including pow(), is overridden, and not defined there
# print (eval ('sqrt(25)', {})) # math's, including sqrt(), is not defined


##########################################
# Defining Global and Local Dictionaries #
##########################################
import math


names = {'sqrt': math.sqrt, 'pi': math.pi, 'x': 5}
print (eval ('dir()', names))  # ['__builtins__', 'pi', 'sqrt', 'x']
print (eval ('pi', names))  # 3.141592653589793
print (eval ('x', names))  # 5
# sqrt() and pi, along with __builtins__ names, are accessible

# print(eval('z', {'x': 5})) # NameError: name 'z' is not defined
print (eval ('z', {'z': 30}))  # 30
# though z is defined inside eval() dictionary, its value is not global to the outside scope
# print(z)  # NameError: name 'z' is not defined

# can change names of methods
names = {'square_root': math.sqrt, 'power': math.pow}
print (eval ('dir()', names))  # ['__builtins__', 'power', 'square_root']
print (eval ('square_root(9)', names))  # 3.0
print (eval ('power(5, 2)', names))  # 25.0

# eval() has no access to math.sqrt(), but access to __builtins__.__import__() opens the door to import any module (including math for example)
print(eval("__import__('math').sqrt(25)", {}, {}))  # 5.0

# can be metigated with:
# print(eval ("__import__('math').sqrt(25)", {'__builtins__': {}}, {})) # NameError: name '__import__' is not defined

# WARNING: sometimes, eval() is not secure even with limited names
# when an object and its methods are made accessible, almost anything can be done with it
# the only secure way is by validating the user input
# one such way could be to prevent executing commands from user input immediately,
# instead, pass the string to a filtering method ('check_eval(user_input)' for example), perform string checks, then execute the commands

#####################
# Practical Example #
#####################

import math


def secret_func():
    return 'Secret key is 1234'


safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith('__')}
# run next code to explore math module and safe_dict' items
# for k, v in (math.__dict__.items ()):
#     print(f'[{k}, {v}]')

print(safe_dict.keys())

# dict_keys(['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log1p', 'log10', 'log2', 'modf', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc', 'prod', 'perm', 'comb', 'nextafter', 'ulp', 'pi', 'e', 'tau', 'inf', 'nan'])

expr = ['x + 3', 'secret_func()']
x = [3, 5]

for i in range(len(expr)):

    try:
        # isolate dictionary from iteration to the other
        safe_dict_copy = safe_dict.copy()
        safe_dict_copy['x'] = x[i]

        y = eval(expr[i], {'__builtins__': None}, safe_dict_copy)

        print(f'evaluation of [{expr[i]}] = [{x[i]}]')
    except:
        print(f'expression [{expr[i]}] is not valid')

# evaluation of [x + 3] = [3]
# expression [secret_func()] is not valid

#########################
# Reading Literals Only #
#########################

from ast import literal_eval


# literal_eval() can safely evaluate a string representing a valid Python expression (representing only bytes, numbers, tuples, lists, dicts, sets, booleans, and None)
print (literal_eval ('15.02'))
# print (literal_eval ('0110101')) # invalid binary expression
print (literal_eval ('110101'))
# print (literal_eval ('(2, 3'))  # invalid set expression
print (literal_eval ('(2, 3)'))
print (literal_eval ('[2, 3]'))
print (literal_eval ('{2, 3}'))
print (literal_eval ("{'a': 2, 'b': 3}"))
print (literal_eval ('True'))
print (literal_eval ('None'))  # Trying to evaluate an expression results in an error
# print(literal_eval ('1 + 1')) # ValueError