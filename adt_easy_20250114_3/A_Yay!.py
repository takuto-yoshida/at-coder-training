"""
A - Yay!

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250114_3/tasks/abc342_a
"""


#main
stdin = input()

just_one_symbol = None
first_char = stdin[0]
second_char = stdin[1]
third_char = stdin[2]


if first_char == second_char : 
    if first_char == third_char :#AAA
        for i in range(len(stdin)):
            if stdin[i] != first_char :
                print(i+1)
                break
    else : #AAB
       print(3)
elif first_char == third_char : #ABA
       print(2)
else :#ABB
       print(1)
     
