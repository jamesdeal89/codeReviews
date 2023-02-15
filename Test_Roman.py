# testing for roman numeral conversions python challenge
from CR_Roman import denToRom, romToDen

def test_denToRom():
    assert denToRom(10) == "X"
    assert denToRom(9167) == "MMMMMMMMMCLXVII"
    assert denToRom(512) == "DXII"
    assert denToRom(38) == "XXXVIII"
    assert denToRom(5) =="V"
    assert denToRom(8) =="VIII"
    assert denToRom(9) =="IX"
    assert denToRom(4) =="IV"

def test_romToDen():
    assert romToDen("X") == 10 
    assert romToDen("MMMMMMMMMCLXVII") == 9167 
    assert romToDen("DXII") == 512
    assert romToDen("XXXVIII") == 38
    assert romToDen("V") == 5
    assert romToDen("VIII") == 8
    assert romToDen("IX") == 9
    assert romToDen("IV") == 4
