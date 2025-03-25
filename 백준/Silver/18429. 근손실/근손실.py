from itertools import permutations

N,K = map(int,input().split())
nums = list(map(int,input().split()))

def permu(n,nums):
    for num in list(permutations(nums,n)):
        yield num

count = 0

for p in permu(N,nums):
    weight = 500
    for day in range(N):
        weight -= K
        weight += p[day]
        if weight < 500:
            break
    else:
        count += 1

print(count)