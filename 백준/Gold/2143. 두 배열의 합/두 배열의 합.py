from sys import stdin
from collections import defaultdict
target = int(stdin.readline())
a_n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
b_n = int(stdin.readline())
b = list(map(int,stdin.readline().split()))


def sub_sum(arr) :
    sums = defaultdict(int)
    for i in range(len(arr)) :
        current_sum = 0
        for j in range(i,len(arr)) :
            current_sum += arr[j]
            sums[current_sum] += 1
    
    return sums

a_sum = sub_sum(a)
b_sum = sub_sum(b)
count = 0
for i in a_sum :
    if target - i in b_sum :
        count += a_sum[i] * b_sum[target-i]

print(count)