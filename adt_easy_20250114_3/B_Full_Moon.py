"""
B - Full Moon 
@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250114_3/tasks/abc318_a

"""


#main
stdin = input()
inputs = stdin.split(" ")

end_day = int(inputs[0])
first_day = int(inputs[1])
days_interval = int(inputs[2])


# first_day + days_interval * (number_of_views-1) = end_day

if end_day < first_day:
    number_of_views = 0
else:
    number_of_views = int((end_day - first_day) / days_interval) + 1

print(number_of_views)