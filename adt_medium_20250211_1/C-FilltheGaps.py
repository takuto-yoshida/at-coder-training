"""
C - Fill the Gaps 

@auth takuto yoshida
https://atcoder.jp/contests/adt_medium_20250211_1/tasks/abc301_b

"""

input()
sequence_str = input().split(" ")

sequence = []
for i in range(len(sequence_str)):
    sequence.append(int(sequence_str[i]))

length = len(sequence)
result_sequence = []
before_number = None

for i in range(length):
    if i == 0:
        before_number = sequence[i]
        result_sequence.append(sequence[i])


    elif i == length - 1:
        result_sequence.append(sequence[i])
        break


    else:
        if sequence[i] > before_number:
            while(sequence[i] != before_number + 1):
                before_number = before_number + 1
                result_sequence.append(before_number)

            before_number = before_number + 1
            result_sequence.append(before_number)


        if sequence[i] < before_number:
            while(sequence[i] != before_number - 1):
                before_number = before_number - 1
                result_sequence.append(before_number)

            before_number = before_number - 1
            result_sequence.append(before_number)


result_sequence = [str(i) for i in result_sequence]
print(" ".join(result_sequence))
