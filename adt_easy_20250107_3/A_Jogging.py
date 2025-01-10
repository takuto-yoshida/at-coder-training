"""
A - Jogging

@auth takuto yoshida
https://atcoder.jp/contests/adt_easy_20250107_3/tasks/abc249_a
"""

def calculate_distance(movetime:int,velocity:int,resttime:int,time:int)->int:

    laptime = movetime + velocity + resttime
    num_of_laps =  int(time // laptime)
    time_remaining = int(time % laptime)
    
    totalmovetime = movetime * num_of_laps
    if time_remaining < movetime:
        totalmovetime = totalmovetime + movetime
    else :
        totalmovetime = totalmovetime + time_remaining

    return totalmovetime * velocity

#main
stdin = input()
inputs = stdin.split(' ')

movetime_takahashi = int(inputs[0])
velocity_takahashi = int(inputs[1])
resttime_takahashi = int(inputs[2])

movetime_aoki= int(inputs[3])
velocity_aoki = int(inputs[4])
resttime_aoki = int(inputs[5])

time = int(inputs[6])

distance_takahashi = calculate_distance(movetime_takahashi,velocity_takahashi,resttime_takahashi,time)
distance_aoki = calculate_distance(movetime_aoki,velocity_aoki,resttime_aoki,time)

if distance_takahashi > distance_aoki:
    result = "Takahashi"
elif distance_takahashi < distance_aoki:
    result = "Aoki"
else:
    result = "Draw"

print(result)
