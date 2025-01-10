"""
B - Pawn on a Grid 

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250107_3/tasks/abc280_a
"""

def count_piece(line:str) -> int:
    PIECE_SYMBOL = "#"

    return line.count(PIECE_SYMBOL)

#main
input_first_line = input()

num_of_rows = int(input_first_line.split(" ")[0]) # 行は本内容では使わない

input_lines = [input() for i in range(num_of_rows)]

result = 0

for line in input_lines:
    result = result + count_piece(line)

print(result)

