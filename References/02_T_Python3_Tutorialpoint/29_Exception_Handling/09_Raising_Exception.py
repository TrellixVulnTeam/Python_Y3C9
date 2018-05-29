


"""

The following example illustrates the use of raising an exception −


"""


def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])

"""

This will produce the following result

error in level argument -10

"""
