# https://www.acmicpc.net/problem/2252

from sys import stdin

N,M = map(int,stdin.readline().split())
advances = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

inter_num = [0 for i in range(N+1)]
nums = {}

for a,b in advances :
    if a in nums :
        nums[a].append(b)
    else :
        nums[a] = [b]
    inter_num[b] +=1

queue = []
for index,value in enumerate(inter_num) :
    if index > 0 and value == 0 :
        queue.append(index)

result = []
while queue :
    current = queue.pop()
    result.append(current)
    if current in nums :
        for i in nums[current]:
            inter_num[i] -= 1
            if inter_num[i] == 0 :
                queue.append(i)

print(" ".join(map(str,result)))