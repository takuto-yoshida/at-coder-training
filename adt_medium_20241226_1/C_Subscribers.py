"""
C - Subscribers 

@auth takuto yoshida
https://atcoder.jp/contests/adt_medium_20241226_1/tasks/abc304_b
"""

def round_down_significant_digits(number_str:str)->int:
    
    SIGNIFICANT_DIGITS = 3
    digits = -(len(number_str)-SIGNIFICANT_DIGITS)

    return round(int(number_str),digits)


#main
stdin = input()

out = round_down_significant_digits(stdin)

print(out)

