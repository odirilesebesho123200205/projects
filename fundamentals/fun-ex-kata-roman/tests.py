from number_representations import to_roman_numeral

roman_numerals = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII',
    13: 'XIII',
    14: 'XIV',
    15: 'XV',
    16: 'XVI',
    17: 'XVII',
    18: 'XVIII',
    19: 'XIX',
    20: 'XX',
    21: 'XXI',
    22: 'XXII',
    23: 'XXIII',
    24: 'XXIV',
    25: 'XXV',
    26: 'XXVI',
    27: 'XXVII',
    28: 'XXVIII',
    29: 'XXIX',
    30: 'XXX',

    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM',
}


def test_roman_numerals():
    for number, ours in roman_numerals.items():
        theirs = to_roman_numeral(number)
        assert theirs == ours, f"Tried {number} -> {ours}, got {theirs}"
