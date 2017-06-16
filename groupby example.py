"""http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/"""

# self has to be in every method in a class
class ClassName
    def __init__(self): # constructor
        self.y = 5 # variable for every instance of method
        self.printName() # method for every instance of ClassName
    def printName(self): # method
        print "Name"

x = ClassName()

def outside(arg):
    x=5
    def printName(arg):
        print x
    return printName

myfunc = outside()
myfunc()

def addOne(myFunc):
    def addOneInside():
        return myFunc() +1
    return addOneInside

def oldfunc():
    return 3

newfunc = addOne(oldFunc)
print oldFunc(), newFunc()
    pass