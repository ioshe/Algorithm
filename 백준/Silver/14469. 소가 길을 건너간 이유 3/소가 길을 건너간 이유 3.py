from sys import stdin


N = int(stdin.readline())
nums = list(map(lambda a : list(map(int,a.split())), stdin.readlines()))
nums.sort(key=lambda x : (-x[0], -x[1]))

time = 0

while nums:
    arrived_time, check_time = nums.pop()
    time = max(time, arrived_time) + check_time

print(time)

 