from sys import stdin

n,m = map(int,stdin.readline().split())
nums = list(map(lambda a: list(map(int,a.split())), stdin.readlines()))

for i in range(n) :
    for j in range(m) :
        if i == 0 and j == 0:
            continue
        if i ==0 :
            nums[i][j] =nums[i][j] + nums[i][j-1]
            continue
        if j == 0 :
             nums[i][j] =nums[i][j] + nums[i-1][j]
             continue
        nums[i][j] = nums[i][j] + max(nums[i-1][j],nums[i][j-1],nums[i-1][j-1])

# print("\n".join(" ".join(map(str,i)) for i in nums))
print(nums[-1][-1])