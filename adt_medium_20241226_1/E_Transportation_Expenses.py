"""
E - Transportation Expenses

@auth takuto yoshida
https://atcoder.jp/contests/adt_medium_20241226_1/tasks/abc365_c

"""

def calc_total_payment(expenses:list[int], subsidy:int) -> int:
    sum = 0
    for expense in expenses:
        if expense < subsidy:
            sum = sum + expense
        else:
            sum = sum + subsidy

    return sum

def search_subsidy(budget:int, num_of_people:int, expenses:list[int]) -> int:
    max_subsidy = budget
    min_subsidy = int(budget / num_of_people)
    left = min_subsidy
    right = max_subsidy
    mid = 0
    while left <= right:
        mid = int((left + right) / 2)
        total_payment = calc_total_payment(expenses,mid)
        #print(f"[debug]subsidy:{mid} total_payment:{total_payment} budget:{budget}")
        if total_payment < budget:
            left = mid + 1
        else:
            right = mid - 1
        
    return mid

#main
first_input = input()
second_line = input()

first_inputs = first_input.split(" ")
num_of_people = int(first_inputs[0])
budget = int(first_inputs[1])

expenses_str = second_line.split(" ")
expenses = list(map(int, expenses_str))

subsidy = None

if sum(expenses) < budget:
    subsidy = "infinite"
else:
    subsidy = search_subsidy(budget,num_of_people,expenses)

print(subsidy)