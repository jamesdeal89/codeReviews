# a module is a file in python which ends with the extension .py
# modules should contain functions which are related to the name of the moduleabs
# e.g random.py contains functions for generating random numbers etc
import random
# below imports only a specific function from a module 
# from math import ceil
# alternatively you can import several specific functions
from math import ceil, floor
# and you can rename a module for efficiency purposes
import time as t
# note that if specific modules are NOT imported, you will have to use an acessor first
random.randint(0,10)
# however if you have imported a specific function, you do not
ceil(float(input("input a float:")))

# functions are a section of code which returns a value 
# def (define) name (parameters 0 or more):
#   next statement indented 
def f():
    return "this is a function"
# a function call creates a new stack frame until it returns or there are no more statements

# defensive programming concepts
# 1) Validate & Verify --> validate - check values | verification - confirm with user
# 2) Make code 'genralisable' --> can be used for many purposes 

# functions which do not return a value are called procedures 
def p():
    print("this is a procedure")

# functions/procedures can be called using their name
p()

# this is a class
class Cat:
    pass

# this is inheritance from a class
class Tabby(Cat):
    pass

# attributes and methods
class Canine:
    # this is a constructor to initalise the class
    def __init__(self):
        # an attribute is a variable which belongs to a class
        self.legLength = 5
        self.toothSharpness = 9
        self.numTeeth = 42
        self.name = "Canine"

    def bark(self):
        print(f"{self.name}: woof")

class dog(Canine):
    def __init__(self,name):
        # super refers to the inherited class
        super.__init__()
        self.name = name

    def bark(self):
        # polymorphism 
        print(f"{self.name}: bark")

# making and instance of a class
# one class can have many instances, each with different attribute values
bobby = Dog("Bobby")
bobby.bark()
print(f"{bobby.name} has {bobby.numTeeth} teeth")

rex = Dog("rex")
rex.bark()
rex.numTeeth += 4
print(f"{rex.name} has {rex.numTeeth} teeth")