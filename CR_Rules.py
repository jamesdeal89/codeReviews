"""
This coding challenge was later revealed to be an implementation of 'cellular automaton'. https://en.wikipedia.org//wiki/Cellular_automaton
Given a set of rules, return a boolean value based on three inputs.
For example:
if a rule 100|1 is set, return 1 if 1,0,0 is input. 
This should be implemented in a class with rules as an attribute.
"""
import random

class Rules():
    def __init__(self, width=60, height=100):
        # initialise the class and et the ruleSet attribute as a dictionary
        self.ruleSet = {}
        self.width = width
        self.height = height

    def inputRules(self,rulesStr):
        # allow user to input rules
        index = 0
        while index <= len(rulesStr) - 4:
            # set the key as the required input and set the value as the required output
            self.ruleSet[rulesStr[index:index+3]] = rulesStr[index+3]
            # change the index start index to be the start of the next required input
            index += 4

    def randomInputs(self):
        # string to hold the current input
        self.inputStr = ""
        for _ in range(self.width):
            # generate a series of random 0 or 1s as per the width
            self.inputStr += str(random.randint(0,1))

    def applyRules(self):
        # list to hold each line after evaluation
        self.allList = []
        for _ in range(self.height):
            self.line = ""
            index = 0
            # loop and apply the rules to each trio
            while index <= len(self.inputStr)-3:
                # apply rule using dictionary, and add it to our output str
                self.line += str(self.ruleSet[self.inputStr[index:index+3]])
                # move the index to the next trio by shifting one value over
                index += 1
            # add the result to our overall list
            self.allList.append(self.line)
            # change the input string to be the result with a leading and following 0
            self.inputStr = "0" + self.line + "0"

    def displayOut(self):
        # for each character in each line print the values nicely
        for line in self.allList:
            for char in line:
                if char == "0":
                    print(" ",end="")
                elif char == "1":
                    print("█",end="")
            # make a new line for each new string
            print()

rules = Rules()
rules.inputRules("11111100101110010110010100110000")
rules.randomInputs()
rules.applyRules()
rules.displayOut()
