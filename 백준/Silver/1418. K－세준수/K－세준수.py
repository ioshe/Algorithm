# https://www.acmicpc.net/problem/1418

N = int(input())
K = int(input())

nums = [i for i in range(N + 1)]
sosu = [1] * (N + 1)

for i in range(2, N + 1):
    for j in range(i * 2, N+1, i):
        sosu[j] = 0
    
for i in range(2, N + 1):
    if sosu[i] != 1:
        continue
    for j in range(i * 2, N+1, i):
        nums[j] = i

print(sum(1 if i <= K else 0 for i in nums[1:]))
# print(nums[1:])