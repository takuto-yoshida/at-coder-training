"""
C - Count Distinct Integers

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250107_3/tasks/abc240_b
"""


#main
input()
input_line = input()

inputs = input_line.split(" ")
unique_numbers_set = set(inputs)
result = len(unique_numbers_set)

print(result)

