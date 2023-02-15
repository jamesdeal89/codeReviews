"""
In this challenge you need to create two functions. 
One which converts roman numerals to denary and vice versa.
"""
def denToRom(den):
    # dictionary to hold the main values for roman numerals 
    # includes explicitly tricky values like 4 and 9 
    dictConvert = {1000:"M",500:"D",100:"C",50:"L",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    output = ""
    # while there is still conversion to do
    while den > 0:
        # for each conversion, large to small
        for value in dictConvert:
            # keep adding the largest possible roman numeral until the remaining den value is too low
            while den - value >= 0:
                output+=dictConvert[value]
                # remove the numeral's value we added and loop
                den -= value
    return output


def romToDen(rom):
    dictConvert = {"M":1000,"D":500,"C":100,"L":50,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    rom = rom.upper()
    # output to hold our denary value
    output = 0
    # tokenise the input to allow for tricky values like IX and IV
    tokens = []
    iterate = 0
    while iterate < len(rom):
        if iterate < len(rom)-1:
            if rom[iterate] == "I" and rom[iterate+1] == "V":
                # add an extra step the iteration to account for the extra value we accounted
                # stop for str splicing is non-inclusive so we have to add 2 instead of 1 here
                tokens.append(rom[iterate:iterate+2])
                iterate += 1
            elif rom[iterate] == "I" and rom[iterate+1] == "X":
                tokens.append(rom[iterate:iterate+2])
                iterate += 1
            else:
                tokens.append(rom[iterate])
        else:
            tokens.append(rom[iterate])
        iterate += 1
    # iterate through every token we made and put them into the dictionary while adding up our denary total
    for token in tokens:
        output += dictConvert[token]
    return output
