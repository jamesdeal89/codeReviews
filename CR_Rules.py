"""
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
        # generate a list of random inputs which are width in length and repeat for height times
        # always leads with a zero for first line if there would be an overflow when divided in trios
        self.inputStr = []
        for _ in range(self.height):
            line = ""
            # create leading 0 if cannot be put into trios
            if self.width % 3:
                line += "0"
            for _ in range(self.width):
                # generate a series of random 0 or 1s as per the width
                line += str(random.randint(0,1))
            # create following 0 if cannot be put into trios
            if self.width % 3:
                line += "0"
            self.inputStr.append(line)


    def applyRules(self):
        # apply the rules to the input list provided
        self.line = ""
        # I made the input list into one large str to make it simpler to account for overflow values
        self.inputStr = "".join(self.inputStr)
        index = 0
        # loop and apply the rules to each trio
        while index <= len(self.inputStr)-3:
            # apply rule using dictionary, and add it to our output str
            self.line += str(self.ruleSet[self.inputStr[index:index+3]])
            # move the index to the next trio
            index += 3

    def displayOut(self):
        for index in range(0,len(self.line)):
            if self.line[index] == "0":
                print(" ",end="")
            elif self.line[index] == "1":
                print("█",end="")
            # seperate into lines of width wide divided by three as this is after applying rules
            if index % (self.width//3)==0:
                print()

rules = Rules()
rules.inputRules("11101101101010010110010100110000")
rules.randomInputs()
rules.applyRules()
rules.displayOut()
