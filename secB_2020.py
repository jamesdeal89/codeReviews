# Section B from 2020
"""
Write a program that asks the user how many numeric digits they would like to enter
and then gets the user to enter that number of numeric digits.
The program should calculate and display the number of times the most frequently
entered numeric digit was input. 
"""

def mode(length):
    # store nums entered
    numbers = []
    # loop for however long user specified
    for _ in range(length):
        # add num to list
        numbers.append(int(input("input num:")))
    counts = {}
    for element in numbers:
        # iterate through and count how many times each value repeats using dict
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1
    for key in counts:
        # iterate through the totals and return whatever key holds a value equal to the max value in the totals dict
        maxVal = max(counts.values())
        if counts[key] == maxVal:
            counts.pop(key)
            # if the max repeats is still the same after removing the old top, there is no single mode
            if max(counts.values()) == maxVal:
                return None
            # if not, return the mode
            else:
                return key



modeVal = mode(int(input("how many lines?:")))
if modeVal != None:
    print(f"mode was :{modeVal}")
else:
    print("Data was multimodal")