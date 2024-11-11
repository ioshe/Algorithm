# https://www.acmicpc.net/problem/10431

from sys import stdin

P = int(stdin.readline())

result = []
for t in range(1,P+1) :
    nums = list(map(int,stdin.readline().split()))[1:]
    count = 0 
    temp = [nums[0]]
    for i in range(1,20) :
        for j in range(i) :
            if nums[i] < temp[j] :
                count += len(temp) - j
                break
        temp.append(nums[i])
        temp.sort()

    result.append([t,count])
    
print("\n".join(map(lambda a : " ".join(map(str,a)),result)))