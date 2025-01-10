"""
D - Taro 

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250107_3/tasks/abc240_b

"""

#main

input_first_line = input()
num_of_babies = int(input_first_line.split(" ")[1]) 
babies = [input() for i in range(num_of_babies)]

families_with_taro = []

for baby in babies:
    family,gender = baby.split(" ")
    isTaro = None
    if gender == "M":
        if family not in families_with_taro:
            families_with_taro.append(family)
            isTaro = True
    
    if isTaro:
        print("Yes")
    else:
        print("No")

