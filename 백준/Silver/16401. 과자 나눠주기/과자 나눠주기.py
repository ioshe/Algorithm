# https://www.acmicpc.net/problem/16401

from sys import stdin

M,N = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

start = 1
end = max(nums)

while start <= end :
    count = 0
    mid = (start + end) // 2
    for i in nums :
        count += i // mid
        if count >= M :
            start = mid + 1
            break
    if count < M :
        end = mid -1

print(end)