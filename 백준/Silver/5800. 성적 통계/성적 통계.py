from sys import stdin

'''
2
5 30 25 76 23 78
6 25 50 70 99 70 90
'''

def proce_scroe(nums) :
    Large = 0 
    for i in range(len(nums)) :
        if i > 0 and Large < nums[i] - nums[i-1] :
            Large = nums[i] - nums[i-1]
    return Large
n = int(stdin.readline())
for i in range(1,n+1) :
    print(f'Class {i}')
    nums = list(map(int,stdin.readline().split()[1:]))
    nums.sort()
    L = proce_scroe(nums)
    print(f'Max {nums[-1]}, Min {nums[0]}, Largest gap {L}')