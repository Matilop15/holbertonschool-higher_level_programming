#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0    
    roman_let = [
            ["I", 1],
            ["V", 5],
            ["X", 10],
            ["L", 50],
            ["C", 100],
            ["D", 500],
            ["M", 1000],
            ]
    num = 0
    last = 0
    for letra in roman_string:
        for elem in roman_let:
            if letra == elem[0]:
                if last == 0 or last >= elem[1]:
                    num += elem[1]
                elif last < elem[1]:
                    num += elem[1] - last

                last = elem[1]
    
                return num
