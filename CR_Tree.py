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
    for x in range(size):
        print(" "*(size-x), end="")
        print("#"*(2*x+1), end="")
        print()
f(7)


