# test file for SecB 2019
from secB_2019 import canMake

def test():
    assert canMake("MEET","MEAT") == False
    assert canMake("PIE","DOG") == False
    assert canMake("PIN","NIPPED") == True
    assert canMake("NINE","ELEPHANTI") == False
    assert canMake("NINE","ELEPHANTINE") == True