#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0

    for x in range(1, 4):
        try:
            if x > a:
                raise Exception('Too far')
            res += (a ** b) / x
        except:
            res += b + a
            break

    return res
