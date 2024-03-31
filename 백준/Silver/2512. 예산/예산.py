# https://www.acmicpc.net/problem/2512

from sys import stdin
n = int(stdin.readline())
budgets =list(map(int,stdin.readline().split()))
total_limit = int(stdin.readline())

start,end = 0,max(budgets)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for budget in budgets :
        if budget > mid :
            total += mid
        else :
            total += budget

    if total > total_limit:
        end = mid - 1
    else:
        start = mid + 1

print(end)