from sys import stdin
n = int(stdin.readline()) 
nums = [*map(int,stdin.readline().split())]
max_num = 0
min_num = nums[0]
result = [0]
for i in range(1,n):
    if min_num > nums[i] :
        min_num = nums[i]
    if nums[i] - min_num > result[i-1] :
        result.append(nums[i] - min_num)
    else :
        result.append(result[i-1])
print(" ".join(map(str,result)))