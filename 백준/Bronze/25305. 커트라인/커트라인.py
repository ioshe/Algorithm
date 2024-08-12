'''
5 2
100 76 85 93 98
'''

n,k = map(int,input().split())
nums = list(map(int,input().split()))
print(sorted(nums,reverse=True)[k-1])

