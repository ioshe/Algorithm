n = int(input())
nums = [0]+[i for i in range(1,n+1)]

for i in range(1,n+1) :
	for j in range(2,int(i**0.5)+1,1) :
			if nums[i] > nums[i-j*j]+1 :
 				nums[i] = nums[i-j*j]+1
print(nums[n])