

"""
What is New in Python 3
The __future__ module
Python 3.x introduced some Python 2-incompatible keywords and features that can be imported via the in-built __future__ module in Python 2. It is recommended to use __future__ imports, if you are planning Python 3.x support for your code.

For example, if we want Python 3.x's integer division behavior in Python 2, add the following import statement.

from __future__ import division
The print Function
Most notable and most widely known change in Python 3 is how the print function is used. Use of parenthesis () with print function is now mandatory. It was optional in Python 2.

print "Hello World" #is acceptable in Python 2
print ("Hello World") # in Python 3, print must be followed by ()
The print() function inserts a new line at the end, by default. In Python 2, it can be suppressed by putting ',' at the end. In Python 3, "end =' '" appends space instead of newline.

print x,           # Trailing comma suppresses newline in Python 2
print(x, end=" ")  # Appends a space instead of a newline in Python 3
Reading Input from Keyboard
Python 2 has two versions of input functions, input() and raw_input(). The input() function treats the received data as string if it is included in quotes '' or "", otherwise the data is treated as number.

In Python 3, raw_input() function is deprecated. Further, the received data is always treated as string.

In Python 2

>>> x = input('something:') 
something:10 #entered data is treated as number
>>> x
10

>>> x = input('something:')
something:'10' #eentered data is treated as string
>>> x
'10'

>>> x = raw_input("something:")
something:10 #entered data is treated as string even without ''
>>> x
'10'

>>> x = raw_input("something:")
something:'10' #entered data treated as string including ''
>>> x
"'10'"

In Python 3

>>> x = input("something:")
something:10
>>> x
'10'

>>> x = input("something:")
something:'10' #entered data treated as string with or without ''
>>> x
"'10'"

>>> x = raw_input("something:") # will result NameError
Traceback (most recent call last):
   File "<pyshell#3>", line 1, in 
  <module>
   x = raw_input("something:")
NameError: name 'raw_input' is not defined
Integer Division
In Python 2, the result of division of two integers is rounded to the nearest integer. As a result, 3/2 will show 1. In order to obtain a floating-point division, numerator or denominator must be explicitly used as float. Hence, either 3.0/2 or 3/2.0 or 3.0/2.0 will result in 1.5

Python 3 evaluates 3 / 2 as 1.5 by default, which is more intuitive for new programmers.

Unicode Representation
Python 2 requires you to mark a string with a u if you want to store it as Unicode.

Python 3 stores strings as Unicode, by default. We have Unicode (utf-8) strings, and 2 byte classes: byte and byte arrays.

xrange() Function Removed
In Python 2 range() returns a list, and xrange() returns an object that will only generate the items in the range when needed, saving memory.

In Python 3, the range() function is removed, and xrange() has been renamed as range(). In addition, the range() object supports slicing in Python 3.2 and later.

raise exceprion
Python 2 accepts both notations, the 'old' and the 'new' syntax; Python 3 raises a SyntaxError if we do not enclose the exception argument in parenthesis.

raise IOError, "file error" #This is accepted in Python 2
raise IOError("file error") #This is also accepted in Python 2
raise IOError, "file error" #syntax error is raised in Python 3
raise IOError("file error") #this is the recommended syntax in Python 3
Arguments in Exceptions
In Python 3, arguments to exception should be declared with 'as' keyword.

except Myerror, err: # In Python2
except Myerror as err: #In Python 3
next() Function and .next() Method
In Python 2, next() as a method of generator object, is allowed. In Python 2, the next() function, to iterate over generator object, is also accepted. In Python 3, however, next(0 as a generator method is discontinued and raises AttributeError.

gen = (letter for letter in 'Hello World') # creates generator object
next(my_generator) #allowed in Python 2 and Python 3
my_generator.next() #allowed in Python 2. raises AttributeError in Python 3
2to3 Utility
Along with Python 3 interpreter, 2to3.py script is usually installed in tools/scripts folder. It reads Python 2.x source code and applies a series of fixers to transform it into a valid Python 3.x code.

Here is a sample Python 2 code (area.py):

def area(x,y = 3.14): 
   a = y*x*x
   print a
   return a

a = area(10)
print "area",a

To convert into Python 3 version:

$2to3 -w area.py

Converted code :

def area(x,y = 3.14): # formal parameters
   a = y*x*x
   print (a)
   return a

a = area(10)
print("area",a)"""
