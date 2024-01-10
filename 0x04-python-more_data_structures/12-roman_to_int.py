def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return (0)
    
    roman_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    res = 0
    prev_val = 0
    
    for char in reversed(roman_string):
        value = roman_val.get(char, 0)
        if value >= prev_val:
            res += value
        else:
            res -= value
        prev_val = value
    
    return (res)
