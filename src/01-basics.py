#!/usr/bin/python3
# First line is used to determine how to execute a script
# First two characters (#!) are known as "shebang"
# On unix directory /bin usually contain core libraries for users
#  while /usr/bin contain "non-core" and in case of emergency
#  whole /usr might be not available

# In Python3 you must use either tabs or spaces to indent code
#  while Python2 allowed mixed characters introducing a lot of problems
# Normally it doesn't matter which option you choose but consider:
# - tabs take less bytes but require editor to know how much indent per tab
# - spaces look the same in every editor but use more bytes
# - what to do when you press backspace and there are spaces for indentation?

###
## Imports
#

# To use libraries (also built-in) you use `import`
import logging
import random


###
## "global-like" objects
#

# You should never use `logging.<anything>` - instead initialize your own logger
log = logging.getLogger(__name__)


###
## Application start
#

log.info('Starting')
# Although python has `print` you should avoid using it - logging is much better
# By the way - it is a bad idea to run anything before all the functions and dependencies are "initialized"


###
## Functions
#

def nop_function():
    '''This is an example function that does nothing
       but it has a multi-line comment
       that describe what it does
       where the first line is usually most important.'''
    log = logging.getLogger(__name__)
    # We should never use the main `logging` which stands for the "root" logger
    log.info("nop_function starts")
    log.debug("nop stands for 'no operation'")
    log.info("nop_function ends")

# The nop_function is only defined - it needs to be called first before it does anything
nop_function


###
## Logging and log levels
#

# log.critical("Use critical/fatal only when your application is just crashing - nothing will work since that message")
# log.error("Use error only when your application failed to work and someone needs to solve the issue")
log.info("Use info to provide important information about your application")
log.debug("Use debug for non-important information that are usually not shown on production servers - unless there is a need to show them")
# log.trace("Some loggers use .trace to store more detailed logs")
# log.trace2("and even .trace2 to more details")
log.log(logging.NOTSET, "Python logging is using NOTSET level for very detailed developer logs")
# You can use `print(dir(log))` to see whatever methods are available for logging

if log.isEnabledFor(logging.INFO):
    log.info("Some very complex computation here: %d", sum(random.sample(range(100000000),10000000)))
    # If your log require a lot of computation
    #  but it is not always logged - there is no reason to compute if given log level is not enabled
    #  thus you might wish to check if given log level is enabled at all
try:
    0/1
except ZeroDivisionError:
    log.exception("We have encounteres an exception - please, ignore it, extraordinary situation but there is nothing wrong about it")
    log.debug("Since this is an expected application state I should NOT log it as an error")


###
## Variables... normally defined before functions
#

number = 1  # Can be changed later
fractional_number = 1.1  # Can be changed but holds fractional part
binary = 0b11011  # 27
octal = 0o33  # 27
hexadecimal = 0x1b  # 27
complex_value = 1.5j  # 1.5j * 1.5j = -2.25
string = 'a string'
another_string = "again a string - this time I'd like to use apostrophe in it"
complex_string = '''this string contains " and ' alltogether'''
unicode_string = u'\u0000'
raw_string = r'raw \n string - the \n is not escaped'
boolean = True  # 0 is also false, non-zero is true
PI = 3.14  # This should not be changed (but can be)
how_to_work_with_null = None  # None is a special type with special meaning and type NoneType

# Collections
an_array = ["first", "second"]  # a list, can be modified, index starts at 0
a_tuple = ("first", "second")  # a tuple is read-only and should not be modified
a_map = {'key0':1, 'key1': "second"}  # a dict (dictionary)
a_set = {'first', 'third', 'second'}  # an unordered collection
# List:  mutable,     ordered, indexed,     can keep duplicates
# Tuple: non-mutable, orgered, indexed,     can keep duplicates
# Set:   mutable, non-ordered, non-indexed, no duplicates
#  by "indexed" we understand that it can be accessed by index and sliced

an_array[0] = '1st'
an_array.append('3rd')
a_tuple = ('1st,' '2nd')  # It cannot mutate but can be replaced
a_map['key0'] = '1st'
a_map['key2'] = '3rd'
a_set.add('4th')

# In python3 you should remember that objects should be hashable
#  it means that there is a method __hash__() that can be used to compare objects (__cmp__, __eq__)
# When migrating from python2 then hashing often needs to be added along with `print 'aaa'`, indentation and other problems
