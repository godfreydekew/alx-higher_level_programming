#!/usr/bin/python3

def roman_to_int(roman_string):
    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    prev_value = r_dict[roman_string[-1]]
    for c in reversed(roman_string):
        current_value = r_dict[c]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
    return int(total)
