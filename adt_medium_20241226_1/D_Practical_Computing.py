"""
D - Practical Computing

@auth takuto yoshida
https://atcoder.jp/contests/adt_medium_20241226_1/tasks/abc254_b
"""

def create_item(i:int, j:int, previous_line:list[int]) -> int:
    if j == 0 or j == i:
        return 1
    else:
        return previous_line[j-1] + previous_line[j]
    
def create_line(i:int, previous_line:list[int]) -> list[int] :
    line = []
    for j in range(i + 1):
        item_j = create_item(i ,j ,previous_line)
        line.append(item_j)
    return line

#main
stdin = input()

size = int(stdin)

previous_line = None

for i in range(size):
    line = create_line(i, previous_line)
    
    line_str = ' '.join([f'{num:1}' for num in line])
    print(line_str)
    
    previous_line = line
    
