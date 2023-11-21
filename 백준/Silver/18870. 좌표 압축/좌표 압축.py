from sys import stdin
n = int(stdin.readline())
nums = [*map(int,stdin.readline().split())]
sort_nums = sorted(list(set(nums)))
x_index = {sort_nums[index] : index for index in range(len(sort_nums))}

result = []
for i in nums :
    result.append(x_index[i])

print(" ".join(map(str,result)))