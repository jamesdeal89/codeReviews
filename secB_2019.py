# Section B from 2019
# get two words from the user and display if first word can be created from the second.

def canMake(word1,word2):
    word1, word2 = list(word1), list(word2)
    if len(word1) <= len(word2):
        for letter in word1:
            if letter in word2:
                    word2.pop(word2.index(letter))
            else:
                return False
        return True
    else:
        return False

#print(canMake(input(""),input("")))