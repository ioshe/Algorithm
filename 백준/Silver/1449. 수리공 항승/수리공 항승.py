from sys import stdin

n,l = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))
nums.sort()
tape_count = 0
count = 0

for num in nums:
    if num > count:
        tape_count += 1
        count = num + l - 1
print(tape_count)