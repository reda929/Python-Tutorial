##################
# Pretty Printer #
##################

# can “pretty-print” arbitrary data structures in a form that can be used as input to the interpreter
# formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the customizable allowed width

# class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True, underscore_numbers=False): construct a PrettyPrinter instance,  with the following:

# indent: amount of indentation added for each nesting level
# width: desired maximum number of characters per line in the output, a best effort will be made if a structure cannot be formatted within the width constraint
# depth: controls the number of nesting levels which may be printed; if the data structure being printed is too deep, the next contained level is replaced by .... (there is no constraint on the depth by default)
# stream (default sys.stdout) is a file-like object to which the output will be written by calling its write() method
# compact impacts the way that long sequences (lists, tuples, sets, etc) are formatted
# if compact is false (default) then each item of a sequence will be formatted on a separate line
# if compact is true, as many items as will fit within the width will be formatted on each output line
# if sort_dicts is true (default), dictionaries will be formatted with their keys sorted
# if sort_dicts is false, dictionaries will display in insertion order
# if underscore_numbers is true, integers will be formatted with the '_' character for a thousands separator
# if underscore_numbers is false, underscores are not displayed (default)

import pprint


indent = 1
width = 80
depth = None
stream = None
compact = True
sort_dicts = True
underscore_numbers = True

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni', 123432985432]
print(stuff)
stuff.insert(0, stuff[:])
print(stuff)
print(f"{'':->{width}}| <- pprint limit")

pp = pprint.PrettyPrinter(compact = True)
pp.pprint(stuff)
pp = pprint.PrettyPrinter(compact = False)
pp.pprint(stuff)

# for i in range(1, 101, 10):
#     pp = pprint.PrettyPrinter(compact = True)
#     pp.pprint(stuff)

"""
############################################
############################################
"""
# The pprint module also provides several shortcut functions:
# pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
# Return the formatted representation of object as a string. indent, width, depth, compact, sort_dicts and underscore_numbers will be passed to the PrettyPrinter constructor as formatting parameters.

# pprint.pp(object, *args, sort_dicts=False, **kwargs)
# Prints the formatted representation of object followed by a newline. If sort_dicts is false (the default), dictionaries will be displayed with their keys in insertion order, otherwise the dict keys will be sorted. args and kwargs will be passed to pprint() as formatting parameters.
"""
############################################
############################################
"""

# pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
# Prints the formatted representation of object on stream, followed by a newline. If stream is None, sys.stdout is used. This may be used in the interactive interpreter instead of the print() function for inspecting values (you can even reassign print = pprint.pprint for use within a scope). indent, width, depth, compact, sort_dicts and underscore_numbers will be passed to the PrettyPrinter constructor as formatting parameters.
# import pprint
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff)
# pprint.pprint(stuff)
# [<Recursion on list with id=...>,
#  'spam',
#  'eggs',
#  'lumberjack',
#  'knights',
#  'ni']
# pprint.isreadable(object)
# Determine if the formatted representation of object is “readable”, or can be used to reconstruct the value using eval(). This always returns False for recursive objects.
#
# >>>
# pprint.isreadable(stuff)
# False
# pprint.isrecursive(object)
# Determine if object requires a recursive representation.
#
# pprint.saferepr(object)
# Return a string representation of object, protected against recursive data structures. If the representation of object exposes a recursive entry, the recursive reference will be represented as <Recursion on typename with id=number>. The representation is not otherwise formatted.
#
# pprint.saferepr(stuff)
# "[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"

"""
############################################
############################################
"""

# PrettyPrinter Objects
# PrettyPrinter instances have the following methods:
#
# PrettyPrinter.pformat(object)
# Return the formatted representation of object. This takes into account the options passed to the PrettyPrinter constructor.
#
# PrettyPrinter.pprint(object)
# Print the formatted representation of object on the configured stream, followed by a newline.
#
# The following methods provide the implementations for the corresponding functions of the same names. Using these methods on an instance is slightly more efficient since new PrettyPrinter objects don’t need to be created.
#
# PrettyPrinter.isreadable(object)
# Determine if the formatted representation of the object is “readable,” or can be used to reconstruct the value using eval(). Note that this returns False for recursive objects. If the depth parameter of the PrettyPrinter is set and the object is deeper than allowed, this returns False.
#
# PrettyPrinter.isrecursive(object)
# Determine if the object requires a recursive representation.
#
# This method is provided as a hook to allow subclasses to modify the way objects are converted to strings. The default implementation uses the internals of the saferepr() implementation.
#
# PrettyPrinter.format(object, context, maxlevels, level)
# Returns three values: the formatted version of object as a string, a flag indicating whether the result is readable, and a flag indicating whether recursion was detected. The first argument is the object to be presented. The second is a dictionary which contains the id() of objects that are part of the current presentation context (direct and indirect containers for object that are affecting the presentation) as the keys; if an object needs to be presented which is already represented in context, the third return value should be True. Recursive calls to the format() method should add additional entries for containers to this dictionary. The third argument, maxlevels, gives the requested limit to recursion; this will be 0 if there is no requested limit. This argument should be passed unmodified to recursive calls. The fourth argument, level, gives the current level; recursive calls should be passed a value less than that of the current call.

"""
############################################
############################################
"""

# Example
# To demonstrate several uses of the pprint() function and its parameters, let’s fetch information about a project from PyPI:
#
# >>>
# >>> import json
# >>> import pprint
# >>> from urllib.request import urlopen
# >>> with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
# ...     project_info = json.load(resp)['info']
# In its basic form, pprint() shows the whole object:
#
# >>>
# >>> pprint.pprint(project_info)
# {'author': 'The Python Packaging Authority',
#  'author_email': 'pypa-dev@googlegroups.com',
#  'bugtrack_url': None,
#  'classifiers': ['Development Status :: 3 - Alpha',
#                  'Intended Audience :: Developers',
#                  'License :: OSI Approved :: MIT License',
#                  'Programming Language :: Python :: 2',
#                  'Programming Language :: Python :: 2.6',
#                  'Programming Language :: Python :: 2.7',
#                  'Programming Language :: Python :: 3',
#                  'Programming Language :: Python :: 3.2',
#                  'Programming Language :: Python :: 3.3',
#                  'Programming Language :: Python :: 3.4',
#                  'Topic :: Software Development :: Build Tools'],
#  'description': 'A sample Python project\n'
#                 '=======================\n'
#                 '\n'
#                 'This is the description file for the project.\n'
#                 '\n'
#                 'The file should use UTF-8 encoding and be written using '
#                 'ReStructured Text. It\n'
#                 'will be used to generate the project webpage on PyPI, and '
#                 'should be written for\n'
#                 'that purpose.\n'
#                 '\n'
#                 'Typical contents for this file would include an overview of '
#                 'the project, basic\n'
#                 'usage examples, etc. Generally, including the project '
#                 'changelog in here is not\n'
#                 'a good idea, although a simple "What\'s New" section for the '
#                 'most recent version\n'
#                 'may be appropriate.',
#  'description_content_type': None,
#  'docs_url': None,
#  'download_url': 'UNKNOWN',
#  'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
#  'home_page': 'https://github.com/pypa/sampleproject',
#  'keywords': 'sample setuptools development',
#  'license': 'MIT',
#  'maintainer': None,
#  'maintainer_email': None,
#  'name': 'sampleproject',
#  'package_url': 'https://pypi.org/project/sampleproject/',
#  'platform': 'UNKNOWN',
#  'project_url': 'https://pypi.org/project/sampleproject/',
#  'project_urls': {'Download': 'UNKNOWN',
#                   'Homepage': 'https://github.com/pypa/sampleproject'},
#  'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
#  'requires_dist': None,
#  'requires_python': None,
#  'summary': 'A sample Python project',
#  'version': '1.2.0'}

"""
############################################
############################################
"""

# The result can be limited to a certain depth (ellipsis is used for deeper contents):
#
# >>>
# >>> pprint.pprint(project_info, depth=1)
# {'author': 'The Python Packaging Authority',
#  'author_email': 'pypa-dev@googlegroups.com',
#  'bugtrack_url': None,
#  'classifiers': [...],
#  'description': 'A sample Python project\n'
#                 '=======================\n'
#                 '\n'
#                 'This is the description file for the project.\n'
#                 '\n'
#                 'The file should use UTF-8 encoding and be written using '
#                 'ReStructured Text. It\n'
#                 'will be used to generate the project webpage on PyPI, and '
#                 'should be written for\n'
#                 'that purpose.\n'
#                 '\n'
#                 'Typical contents for this file would include an overview of '
#                 'the project, basic\n'
#                 'usage examples, etc. Generally, including the project '
#                 'changelog in here is not\n'
#                 'a good idea, although a simple "What\'s New" section for the '
#                 'most recent version\n'
#                 'may be appropriate.',
#  'description_content_type': None,
#  'docs_url': None,
#  'download_url': 'UNKNOWN',
#  'downloads': {...},
#  'home_page': 'https://github.com/pypa/sampleproject',
#  'keywords': 'sample setuptools development',
#  'license': 'MIT',
#  'maintainer': None,
#  'maintainer_email': None,
#  'name': 'sampleproject',
#  'package_url': 'https://pypi.org/project/sampleproject/',
#  'platform': 'UNKNOWN',
#  'project_url': 'https://pypi.org/project/sampleproject/',
#  'project_urls': {...},
#  'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
#  'requires_dist': None,
#  'requires_python': None,
#  'summary': 'A sample Python project',
#  'version': '1.2.0'}

"""
############################################
############################################
"""

# Additionally, maximum character width can be suggested. If a long object cannot be split, the specified width will be exceeded:
#
# >>>
# >>> pprint.pprint(project_info, depth=1, width=60)
# {'author': 'The Python Packaging Authority',
#  'author_email': 'pypa-dev@googlegroups.com',
#  'bugtrack_url': None,
#  'classifiers': [...],
#  'description': 'A sample Python project\n'
#                 '=======================\n'
#                 '\n'
#                 'This is the description file for the '
#                 'project.\n'
#                 '\n'
#                 'The file should use UTF-8 encoding and be '
#                 'written using ReStructured Text. It\n'
#                 'will be used to generate the project '
#                 'webpage on PyPI, and should be written '
#                 'for\n'
#                 'that purpose.\n'
#                 '\n'
#                 'Typical contents for this file would '
#                 'include an overview of the project, '
#                 'basic\n'
#                 'usage examples, etc. Generally, including '
#                 'the project changelog in here is not\n'
#                 'a good idea, although a simple "What\'s '
#                 'New" section for the most recent version\n'
#                 'may be appropriate.',
#  'description_content_type': None,
#  'docs_url': None,
#  'download_url': 'UNKNOWN',
#  'downloads': {...},
#  'home_page': 'https://github.com/pypa/sampleproject',
#  'keywords': 'sample setuptools development',
#  'license': 'MIT',
#  'maintainer': None,
#  'maintainer_email': None,
#  'name': 'sampleproject',
#  'package_url': 'https://pypi.org/project/sampleproject/',
#  'platform': 'UNKNOWN',
#  'project_url': 'https://pypi.org/project/sampleproject/',
#  'project_urls': {...},
#  'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
#  'requires_dist': None,
#  'requires_python': None,
#  'summary': 'A sample Python project',
#  'version': '1.2.0'}