"""
C - First Query Problem

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250128_1/tasks/abc283_b

"""

#main

def get_sequence_value(sequence,index:int):
    return sequence[index]

def replace_sequence_value(sequence,index,value):
    sequence[index] = value
    return sequence

number_of_sequence = int(input())
sequence = input().split(" ")
qty = int(input())
queries = []
for i in range(qty):
    queries.append(input().split(" "))

for query in queries:
    if query[0] == "1": #1なら置き換え
        index = int(query[1]) - 1
        value = query[2]
        sequence = replace_sequence_value(sequence,index,value)

    if query[0] == "2": #2なら表示
        index = int(query[1]) - 1
        value = get_sequence_value(sequence,index)
        print(value)

    


