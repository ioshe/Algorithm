target = int(input())
MAX=50000
nums= [0]*(target+1)
nums[1]=1
for i in range(2,target+1) :
    nums[i] = nums[i-1]+1
    for j in range(1,int(i**0.5)+1) :
        nums[i] = min(nums[i],nums[i-j**2]+1)
print(nums[target])