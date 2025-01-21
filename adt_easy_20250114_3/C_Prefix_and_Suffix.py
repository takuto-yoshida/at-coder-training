"""
C - Prefix and Suffix
@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250114_3/tasks/abc322_b


"""

def is_prefix(target:str , pattern_piece:str) -> bool:
    for i in range(len(pattern_piece)):
        if target[i] != pattern_piece[i]:
            return False

    # 最後までFalseでないならTrue
    return True

def is_suffix(target:str , pattern_piece:str) -> bool:
    # 後ろからindexを図るため1を引いておく
    target_baseindex = len(target) - 1 
    pattern_piece_baseindex = len(pattern_piece) - 1

    for i in range(len(pattern_piece)):
        if target[target_baseindex - i] != pattern_piece[pattern_piece_baseindex - i]:
            return False

    # 最後までFalseでないならTrue
    return True

#main
first_stdin = input() # 1行目はすてる
pattern_piece = input()
target = input()

prefix_flag = is_prefix(target, pattern_piece)
suffix_flag = is_suffix(target, pattern_piece)

if prefix_flag & suffix_flag:
    print(0) 
elif prefix_flag :
    print(1)
elif suffix_flag : 
    print(2)
else:
    print(3)

