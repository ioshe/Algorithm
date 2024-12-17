from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readlines()))
    
nums.sort()

max_cnt = 1
for i in range(n):
    exist = [0 for i in range(5)]
    cnt = 1
    for j in range(i+1,min(n,i+5)):
        temp = nums[j] - nums[i] 
        if temp <= 4 and not(exist[temp]) :
            exist[temp] = 1
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    
print(5 - max_cnt)