from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
disk = int(stdin.readline())
count = 0
for i in nums :
    if i != 0 :
        count += ((i // disk) + (1 if i % disk else 0))

print(disk * count)
        