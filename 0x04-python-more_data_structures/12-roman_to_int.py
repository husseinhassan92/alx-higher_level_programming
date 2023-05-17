#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    number = list(roman_string)
    result = 0
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(number)):
        if (i != len(number) - 1) and (num[number[i]] < num[number[i + 1]]):
            result -= num[number[i]]
        else:
            result += num[number[i]]
    return result
