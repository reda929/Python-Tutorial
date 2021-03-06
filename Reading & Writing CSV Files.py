##########################
# Comma Separated Values #
##########################

# CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases
# there has not been consistent, well-defined standard (including delimiters and overall format) used by different parties producing and consuming data
# csv module implements classes to read and write tabular data in CSV format (sometimes, even without knowing what format an application uses, like “write in format preferred by Excel,” or “read in the same format used by Excel”
# can also allow programmers interpret custom CSV formats used by other applications, or define the CSV formats themselves

import csv

#####################
# Reading CSV Files #
#####################

# csv.reader(csvfile, dialect='excel', **fmtparams): returns a reader object which will iterate over lines, parsing lines using delimiter strings, in the csvfile file
# csvfile can be any object that supports the iterator protocol
# if csvfile is a file object, it should be opened with newline=''
# optional dialect parameter defines reading parameters
# other optional keyword-arguments fmtparams parameters can override individual formatting parameters in the given dialect
# each row read is returned as a list of strings, which may be converted depending on quoting option provided

print('reading csv: ')
with open('eggs.csv', newline = '') as csvfile:
    csvr = csv.reader(csvfile)
    for row in csvr:
        print(f'{row}')

########################
# Writing to CSV Files #
########################

# csv.writer(csvfile, dialect='excel', **fmtparams): returns a writer object converting the later input data into delimited strings on the given csvfile file
# csvfile can be any object with a write() method
# if csvfile is a file object, it should be opened with newline=''
# optional dialect parameter defines writing parameters
# other optional keyword-arguments fmtparams parameters can override individual formatting parameters in the given dialect

print('writing to csv: ')
with open('eggs.csv', 'w', newline = '') as csvfile:
    csvw = csv.writer(csvfile)
    csvw.writerow(['Spam'] * 5 + ['Baked Beans'])
    csvw.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

######################################
# Dialects and Formatting Parameters #
######################################

# a dialect is a class defining formatting reading and writing parameters, including strings separating fields

# Dialect.delimiter: a one-character string used to separate fields (defaults to ',')

# Dialect.doublequote: controls how instances of quotechar appearing inside a field should themselves be quoted (defaults to True). when True, the character is doubled. when False, the escapechar is used as a prefix to the quotechar. on output, if doublequote is False and no escapechar is set, Error is raised if a quotechar is found in a field

# Dialect.escapechar: a one-character string used by the writer to escape the delimiter if quoting is set to QUOTE_NONE and the quotechar if doublequote is False (defaults to None, which disables escaping). on reading, the escapechar removes any special meaning from the following character

# Dialect.lineterminator: the string used to terminate lines produced by the writer (defaults to '\r\n'). the reader is hard-coded to recognise either '\r' or '\n' as end-of-line, and ignores lineterminator

# Dialect.quotechar: a one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters (defaults to '"')

# Dialect.quoting: controls when quotes should be generated by the writer and omitted by the reader. defaults to QUOTE_MINIMAL, but can take on any of the following values:
#   csv.QUOTE_ALL: instructs writer objects to quote all fields
#   csv.QUOTE_MINIMAL: instructs writer objects to only quote those fields which contain special characters such as delimiter, quotechar or any of the characters in lineterminator
#   csv.QUOTE_NONNUMERIC: instructs writer objects to quote all non-numeric fields, and instructs the reader to convert all non-quoted fields to type float
#   csv.QUOTE_NONE: instructs writer objects to never quote fields. When the current delimiter occurs in output data it is preceded by the current escapechar character. If escapechar is not set, the writer will raise Error if any characters that require escaping are encountered. instructs reader to perform no special processing of quote characters

# Dialect.skipinitialspace: when True, strings are trimmed of spaces

# Dialect.strict: when True, raise exception Error on bad CSV input (default to False)

# can define custom dialects
d = {'lineterminator': '\r\n', 'quoting': csv.QUOTE_ALL, 'doublequote': False, 'delimiter': ' ', 'quotechar': '0', 'skipinitialspace': True, 'strict': True}
csv.register_dialect('my_dialect', **d)
#     csvr = csv.reader(csvfile)
#     csvw = csv.writer(csvfile)

# listing dialects
print(csv.list_dialects()) # ['excel', 'excel-tab', 'unix', 'my_dialect']