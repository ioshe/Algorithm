# https://www.acmicpc.net/problem/6236
from sys import stdin

n,m = map(int,stdin.readline().split())
nums = list(map(int,stdin.read().splitlines()))

start = max(nums)
end = sum(nums)



while start <= end :
    mid = (start + end) // 2
    deposit_count = 1
    balance = mid
    for i in nums :
        if balance  < i :
            balance = mid 
            deposit_count += 1
        balance -= i


    if deposit_count <= m :
        end = mid - 1
    else :
        start = mid + 1

print(start)


