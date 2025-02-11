"""
A - chukodai

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250128_1/tasks/abc236_a

英小文字からなる文字列 
S が与えられます。

S の先頭から 
a 文字目と  
b 文字目を入れ替えて得られる文字列を出力してください。

"""

def change_word(target_string:str,left_word_number:int,right_word_number:int):
    left_i = left_word_number - 1
    right_i = right_word_number - 1
    result_string = ""
    for i in range(len(target_string)):
        if i == left_i:
            result_string = result_string + target_string[right_i];
        elif i == right_i:
            result_string = result_string + target_string[left_i];
        else:
            result_string = result_string + target_string[i];
    
    return result_string

#main

s = input()
input_second_line = input()

a,b = input_second_line.split(" ")

target_string = s
left_word_number = int(a) 
right_word_number = int(b)

result_string = change_word(target_string , left_word_number , right_word_number)

print(result_string)
