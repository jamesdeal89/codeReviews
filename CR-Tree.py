# Code Review 1 - Tree
# Given an int parameter, print a 'tree' of # symbols
# Example:
"""
f(7)
      #
     ###
    #####
   #######
  #########
 ###########
#############
"""

def f(size):
    spaces = size-1
    length = 1
    for x in range(size):
        print(" "*spaces, end="")
        print("#"*length, end="")
        spaces -= 1
        length += 2
        print()

f(7)
