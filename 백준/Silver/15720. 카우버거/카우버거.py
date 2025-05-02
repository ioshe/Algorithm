# https://www.acmicpc.net/problem/15720

from sys import stdin

n = min(map(int,stdin.readline().split()))
nums = list(map(lambda a : sorted(list(map(int,a.split())), reverse=True), stdin.readlines()))
# print(nums)
print(sum(map(lambda a : sum(a),nums)))
result = 0
temp = 0
for i in nums:
    for j in range(len(i)):
        if j < n :
            result += i[j]
        else : 
            temp += i[j]

print(int(result * 0.9) + temp)