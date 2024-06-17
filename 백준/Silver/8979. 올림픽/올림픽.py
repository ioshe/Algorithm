from sys import stdin

'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
'''

N,K = map(int,stdin.readline().split())
nums = list(map(lambda a: list(map(int,a.split())),stdin.readlines()))

nums.sort(key = lambda a : (-a[1],-a[2],-a[3]))

i = 1
rank = 1
dupli = 0
# rank = [0 for i in range(N)]
#print(nums)
while i < N :    
    if nums[i][1:] == nums[i-1][1:] :
        dupli += 1
        # rank[nums[i][0]] = i
    else :
        rank += dupli 
        dupli = 0
        rank += 1
        # rank[nums[i][0]] = i
    
    if nums[i][0] == K :
        print(rank)
        break

    i+=1
    