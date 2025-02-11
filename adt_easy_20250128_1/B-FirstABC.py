"""
B - First ABC

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250128_1/tasks/abc311_a

"""

def count_number(target_string:str) -> int:
    
    has_a = False
    has_b = False
    has_c = False

    number = 0
    for chr in target_string:
        if chr == "A":
            has_a = True
        if chr == "B":
            has_b = True
        if chr == "C":
            has_c = True
        
        number = number + 1
        if has_a & has_b & has_c:
            break
    
    return number

#main

input() #一行目は不要
target_string = input()

result_number = count_number(target_string)

print(result_number)
