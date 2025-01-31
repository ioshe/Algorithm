import sys

nums = list(map(int, sys.stdin.readlines()[1:]))
nums.sort(reverse=True)

hap = sum(max(num - i, 0) for i, num in enumerate(nums))
print(hap)